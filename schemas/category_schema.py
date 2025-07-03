


from flask_marshmallow import Marshmallow
from models.categories import Category

ma = Marshmallow()

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
