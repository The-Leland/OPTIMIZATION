


from flask import request, jsonify
from db import session
from util.reflection import populate_object
from models.company import Company, company_schema, companies_schema
import uuid

def create_company():
    data = request.get_json()
    company = Company()
    company.company_id = str(uuid.uuid4())
    populate_object(company, data)
    session.add(company)
    try:
        session.commit()
    except:
        session.rollback()
        return jsonify({"message": "Unable to create company"}), 400
    return jsonify({"message": "Company created", "company_id": company.company_id}), 201

def get_all_companies():
    companies = session.query(Company).all()
    return jsonify(companies_schema.dump(companies)), 200

def get_company_by_id(company_id):
    company = session.query(Company).filter(Company.company_id == company_id).first()
    if not company:
        return jsonify({"message": "Company not found"}), 404
    return jsonify(company_schema.dump(company)), 200

def update_company(company_id):
    company = session.query(Company).filter(Company.company_id == company_id).first()
    if not company:
        return jsonify({"message": "Company not found"}), 404
    data = request.get_json()
    populate_object(company, data)
    try:
        session.commit()
    except:
        session.rollback()
        return jsonify({"message": "Unable to update company"}), 400
    return jsonify({"message": "Company updated", "company": company_schema.dump(company)}), 200

def delete_company(company_id):
    company = session.query(Company).filter(Company.company_id == company_id).first()
    if not company:
        return jsonify({"message": "Company not found"}), 404
    try:
        session.query(Product).filter(Product.company_id == company_id).delete()
        session.delete(company)
        session.commit()
    except:
        session.rollback()
        return jsonify({"message": "Unable to delete company"}), 400
    return jsonify({"message": "Company and related products deleted"}), 200
