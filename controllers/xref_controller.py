


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
            values = {
                col.name: val for col, val in zip(
                    ProductCategoryXref.c,
                    [product_id if col.name == "product_id" else category_id for col in ProductCategoryXref.c]
                ) if col.name in ["product_id", "category_id"]
            }
            stmt = insert(ProductCategoryXref).values(**values)
            session.execute(stmt)

    session.commit()
    return jsonify({"message": "Categories added to product"}), 200
