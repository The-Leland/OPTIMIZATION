

from flask import jsonify
from sqlalchemy import select, join
from db import session
from util.reflection import Product, Warranty, ProductCategoryXref, Category

def get_all_products():
    stmt = select(Product)
    products = session.execute(stmt).fetchall()

    results = []
    for row in products:
        product = row._mapping
        product_dict = {
            col.name: product[col.name]
            for col in Product.c
            if col.name in product
        }

        warranty_row = session.execute(
            select(Warranty).where(Warranty.c.product_id == product_dict['product_id'])
        ).first()
        if warranty_row:
            warranty = warranty_row._mapping
            warranty_dict = {
                col.name: warranty[col.name]
                for col in Warranty.c
                if col.name in warranty
            }
            product_dict["warranty"] = warranty_dict

        category_joins = (
            select(Category)
            .select_from(
                join(ProductCategoryXref, Category,
                     ProductCategoryXref.c.category_id == Category.c.category_id)
            )
            .where(ProductCategoryXref.c.product_id == product_dict['product_id'])
        )
        category_rows = session.execute(category_joins).fetchall()
        product_dict["categories"] = [
            {
                col.name: category[col.name]
                for col in Category.c
                if col.name in category
            }
            for category in [row._mapping for row in category_rows]
        ]

        results.append(product_dict)

    return jsonify(results), 200
