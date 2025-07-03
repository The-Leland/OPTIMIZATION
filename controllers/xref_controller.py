


from flask import request, jsonify
from sqlalchemy import insert, select
from db import session
from util.reflection import ProductCategoryXref

def add_categories_to_product(product_id):
    data = request.get_json()
    category_ids = data.get("category_ids", [])

    for category_id in category_ids:
        exists = session.execute(
            select(ProductCategoryXref).where(
                ProductCategoryXref.c.product_id == product_id,
                ProductCategoryXref.c.category_id == category_id
            )
        ).first()
        if not exists:
            session.execute(insert(ProductCategoryXref).values(
                product_id=product_id, category_id=category_id
            ))

    session.commit()
    return jsonify({"message": "Categories added to product"}), 200
