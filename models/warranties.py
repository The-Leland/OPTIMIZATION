

from db import db
import uuid

class Warranty(db.Model):
    __tablename__ = 'warranties'

    warranty_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String, db.ForeignKey('products.product_id'), nullable=False)
    warranty_months = db.Column(db.String, nullable=False)
