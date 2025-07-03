


from flask import request, jsonify
from sqlalchemy import select, insert, update, delete
from db import session
from util.reflection import Company, Product
import uuid

def create_company():
    
    data = request.get_json()
    company_id = str(uuid.uuid4())

    stmt = insert(Company).values(
        company_id=company_id,
        company_name=data['company_name']
    )
    session.execute(stmt)
    session.commit()
    return jsonify({"message": "Company created", "company_id": company_id}), 201

def get_all_companies():

    stmt = select(Company)
    result = session.execute(stmt).fetchall()
    companies = [dict(row._mapping) for row in result]
    return jsonify(companies), 200

def get_company_by_id(company_id):

    stmt = select(Company).where(Company.c.company_id == company_id)
    company = session.execute(stmt).first()
    if not company:
        return jsonify({"message": "Company not found"}), 404
    return jsonify(dict(company._mapping)), 200

def update_company(company_id):

    data = request.get_json()
    stmt = update(Company).where(Company.c.company_id == company_id).values(**data)
    session.execute(stmt)
    session.commit()
    return jsonify({"message": "Company updated"}), 200

def delete_company(company_id):
    
    session.execute(delete(Product).where(Product.c.company_id == company_id))
    session.execute(delete(Company).where(Company.c.company_id == company_id))
    session.commit()
    return jsonify({"message": "Company and related products deleted"}), 200
