


from db import db
import uuid

class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_id = db.Column(db.String, db.ForeignKey('companies.company_id'), nullable=False)
    company_name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    active = db.Column(db.Boolean, default=True)

    warranty = db.relationship("Warranty", backref="product", uselist=False, cascade="all, delete-orphan")
    categories = db.relationship("ProductCategoryXref", backref="product", cascade="all, delete")
