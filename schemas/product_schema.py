


from extensions import ma
from models.products import Products

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        include_relationships = True
        load_instance = True

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
