


from flask import request, jsonify
from sqlalchemy import select, insert, update, delete
from db import session
from util.reflection import Category, ProductCategoryXref
import uuid

def create_category():
    data = request.get_json()
    category_id = str(uuid.uuid4())

    stmt = insert(Category).values(
        category_id=category_id,
        category_name=data['category_name']
    )
    session.execute(stmt)
    session.commit()
    return jsonify({"message": "Category created", "category_id": category_id}), 201

def get_all_categories():
    stmt = select(Category)
    result = session.execute(stmt).fetchall()
    return jsonify([dict(row._mapping) for row in result]), 200

def get_category_by_id(category_id):
    stmt = select(Category).where(Category.c.category_id == category_id)
    result = session.execute(stmt).first()
    if not result:
        return jsonify({"message": "Category not found"}), 404
    return jsonify(dict(result._mapping)), 200

def update_category(category_id):
    data = request.get_json()
    stmt = update(Category).where(Category.c.category_id == category_id).values(**data)
    session.execute(stmt)
    session.commit()
    return jsonify({"message": "Category updated"}), 200

def delete_category(category_id):
    session.execute(delete(ProductCategoryXref).where(ProductCategoryXref.c.category_id == category_id))
    session.execute(delete(Category).where(Category.c.category_id == category_id))
    session.commit()
    return jsonify({"message": "Category and related xrefs deleted"}), 200
