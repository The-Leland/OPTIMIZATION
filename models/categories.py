


from db import db
import uuid

class Company(db.Model):
    __tablename__ = 'companies'

    company_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_name = db.Column(db.String, unique=True, nullable=False)

    products = db.relationship("Product", backref="company", cascade="all, delete")
