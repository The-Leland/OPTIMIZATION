


from db import db

class ProductCategoryXref(db.Model):
    __tablename__ = 'products_categories_xref'

    product_id = db.Column(db.String, db.ForeignKey('products.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('categories.category_id'), primary_key=True)
