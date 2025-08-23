

from extensions import ma
from models.companies import Companies

class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Companies
        load_instance = True

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)
