

from flask_marshmallow import Marshmallow
from models.companies import Company

ma = Marshmallow()

class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        load_instance = True


