


from extensions import ma
from models.categories import Categories

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categories
        load_instance = True

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
