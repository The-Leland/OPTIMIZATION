


from flask import Blueprint
from controllers import product_controller

product_bp = Blueprint('product_bp', __name__)

product_bp.route('/product', methods=['POST'])(product_controller.create_product)
product_bp.route('/products', methods=['GET'])(product_controller.get_all_products)
product_bp.route('/product/<product_id>', methods=['GET'])(product_controller.get_product_by_id)
