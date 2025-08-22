


from db import db
import uuid

class Category(db.Model):
    __tablename__ = 'categories'

    category_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    category_name = db.Column(db.String, unique=True, nullable=False)

    products = db.relationship("ProductCategoryXref", backref="category", cascade="all, delete")
