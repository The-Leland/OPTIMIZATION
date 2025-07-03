


from .product_routes import product_bp
from .company_routes import company_bp
from .category_routes import category_bp
from .warranty_routes import warranty_bp
from .xref_routes import xref_bp

def register_routes(app):
    app.register_blueprint(product_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(warranty_bp)
    app.register_blueprint(xref_bp)
