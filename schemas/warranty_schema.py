


from flask_marshmallow import Marshmallow
from models.warranties import Warranty

ma = Marshmallow()

class WarrantySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Warranty
        load_instance = True


