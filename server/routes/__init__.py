from .customer import Customer_resource
from .product import Product_resource


def setup_routes(app):
    cr = Customer_resource(app, '/customers/')
    cr.setup()
    pr = Product_resource(app, '/products/')
    pr.setup()
