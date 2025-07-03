


from flask import Blueprint
from controllers import warranty_controller

warranty_bp = Blueprint('warranty_bp', __name__)

warranty_bp.route('/warranty', methods=['POST'])(warranty_controller.create_warranty)
warranty_bp.route('/warranty/<warranty_id>', methods=['GET'])(warranty_controller.get_warranty_by_id)
warranty_bp.route('/warranty/<warranty_id>', methods=['PUT'])(warranty_controller.update_warranty)
warranty_bp.route('/warranty/delete/<warranty_id>', methods=['DELETE'])(warranty_controller.delete_warranty)
