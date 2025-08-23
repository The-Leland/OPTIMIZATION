

from flask import jsonify, request
from db import session
from util.reflection import populate_object
from models.products import Products, product_schema, products_schema
from models.warranties import Warranties, warranty_schema
from models.categories import Categories, category_schema
from models.product_category_xref import ProductCategoryXref

def get_all_products():
    products = session.query(Products).all()
    results = []

    for product in products:
        product_dict = product_schema.dump(product)

        warranty = session.query(Warranties).filter(Warranties.product_id == product.product_id).first()
        if warranty:
            product_dict['warranty'] = warranty_schema.dump(warranty)

        # Fetch categories via the association table
        categories = (
            session.query(Categories)
            .join(ProductCategoryXref, Categories.category_id == ProductCategoryXref.category_id)
            .filter(ProductCategoryXref.product_id == product.product_id)
            .all()
        )
        product_dict['categories'] = categories_schema.dump(categories)

        results.append(product_dict)

    return jsonify(results), 200

def get_product_by_id(product_id):
    product = session.query(Products).filter(Products.product_id == product_id).first()
    if not product:
        return jsonify({"message": "Product not found"}), 404

    product_dict = product_schema.dump(product)

    warranty = session.query(Warranties).filter(Warranties.product_id == product.product_id).first()
    if warranty:
        product_dict['warranty'] = warranty_schema.dump(warranty)

    categories = (
        session.query(Categories)
        .join(ProductCategoryXref, Categories.category_id == ProductCategoryXref.category_id)
        .filter(ProductCategoryXref.product_id == product.product_id)
        .all()
    )
    product_dict['categories'] = categories_schema.dump(categories)

    return jsonify(product_dict), 200

def create_product():
    data = request.get_json()
    product = Products()
    populate_object(product, data)

    session.add(product)
    try:
        session.commit()
    except:
        session.rollback()
        return jsonify({"message": "Unable to create product"}), 400

    return jsonify({"message": "Product created", "product": product_schema.dump(product)}), 201

def update_product_by_id(product_id):
    product = session.query(Products).filter(Products.product_id == product_id).first()
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()
    populate_object(product, data)

    try:
        session.commit()
    except:
        session.rollback()
        return jsonify({"message": "Unable to update product"}), 400

    return jsonify({"message": "Product updated", "product": product_schema.dump(product)}), 200

def delete_product(product_id):
    product = session.query(Products).filter(Products.product_id == product_id).first()
    if not product:
        return jsonify({"message": "Product not found"}), 404

    try:
        session.query(ProductCategoryXref).filter(ProductCategoryXref.product_id == product_id).delete()
        session.query(Warranties).filter(Warranties.product_id == product_id).delete()
        session.delete(product)
        session.commit()
    except:
        session.rollback()
        return jsonify({"message": "Unable to delete product"}), 400

    return jsonify({"message": "Product and related records deleted"}), 200
