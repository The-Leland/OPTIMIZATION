


from extensions import ma
from models.warranties import Warranties

class WarrantySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Warranties
        load_instance = True

warranty_schema = WarrantySchema()
warranties_schema = WarrantySchema(many=True)
