


from flask import Blueprint
from controllers import company_controller

company_bp = Blueprint('company_bp', __name__)

company_bp.route('/company', methods=['POST'])(company_controller.create_company)
company_bp.route('/companies', methods=['GET'])(company_controller.get_all_companies)
company_bp.route('/company/<company_id>', methods=['GET'])(company_controller.get_company_by_id)
company_bp.route('/company/<company_id>', methods=['PUT'])(company_controller.update_company)
company_bp.route('/company/delete/<company_id>', methods=['DELETE'])(company_controller.delete_company)
