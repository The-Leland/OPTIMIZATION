

from flask import request, jsonify
from db import session
from util.reflection import populate_object
from models.category import Category
import uuid

def create_category():
    data = request.get_json()
    category = Category()
    category.category_id = str(uuid.uuid4())
    populate_object(category, data)
    session.add(category)
    session.commit()
    return jsonify({"message": "Category created", "category_id": category.category_id}), 201

def get_all_categories():
    categories = session.query(Category).all()
    return jsonify([category.to_dict() for category in categories]), 200

def get_category_by_id(category_id):
    category = session.query(Category).filter(Category.category_id == category_id).first()
    if not category:
        return jsonify({"message": "Category not found"}), 404
    return jsonify(category.to_dict()), 200

def update_category(category_id):
    category = session.query(Category).filter(Category.category_id == category_id).first()
    if not category:
        return jsonify({"message": "Category not found"}), 404
    data = request.get_json()
    populate_object(category, data)
    session.commit()
    return jsonify({"message": "Category updated"}), 200

def delete_category(category_id):
    session.query(ProductCategoryXref).filter(ProductCategoryXref.category_id == category_id).delete()
    session.query(Category).filter(Category.category_id == category_id).delete()
    session.commit()
    return jsonify({"message": "Category and related xrefs deleted"}), 200
