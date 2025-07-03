


from flask_marshmallow import Marshmallow
from models.products import Product

ma = Marshmallow()

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_relationships = True
        load_instance = True
