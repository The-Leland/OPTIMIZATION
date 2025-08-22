


from flask import Blueprint
from controllers import category_controller

category_bp = Blueprint('category_bp', __name__)

category_bp.route('/category', methods=['POST'])(category_controller.create_category)
category_bp.route('/categories', methods=['GET'])(category_controller.get_all_categories)
category_bp.route('/category/<category_id>', methods=['GET'])(category_controller.get_category_by_id)
category_bp.route('/category/<category_id>', methods=['PUT'])(category_controller.update_category)
category_bp.route('/category/delete/<category_id>', methods=['DELETE'])(category_controller.delete_category)
