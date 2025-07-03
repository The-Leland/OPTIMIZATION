

from flask import request, jsonify
from sqlalchemy import select, insert, update, delete
from db import session
from util.reflection import Warranty
import uuid

def create_warranty():
    data = request.get_json()
    warranty_id = str(uuid.uuid4())

    stmt = insert(Warranty).values(
        warranty_id=warranty_id,
        product_id=data['product_id'],
        warranty_months=data['warranty_months']
    )
    session.execute(stmt)
    session.commit()
    return jsonify({"message": "Warranty created", "warranty_id": warranty_id}), 201

def get_warranty_by_id(warranty_id):
    stmt = select(Warranty).where(Warranty.c.warranty_id == warranty_id)
    warranty = session.execute(stmt).first()
    if not warranty:
        return jsonify({"message": "Warranty not found"}), 404
    return jsonify(dict(warranty._mapping)), 200

def update_warranty(warranty_id):
    data = request.get_json()
    stmt = update(Warranty).where(Warranty.c.warranty_id == warranty_id).values(**data)
    session.execute(stmt)
    session.commit()
    return jsonify({"message": "Warranty updated"}), 200

def delete_warranty(warranty_id):
    stmt = delete(Warranty).where(Warranty.c.warranty_id == warranty_id)
    session.execute(stmt)
    session.commit()
    return jsonify({"message": "Warranty deleted"}), 200
