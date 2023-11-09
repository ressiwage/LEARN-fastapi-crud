from utils import bind_to_app
class Customer_resource:
    _prefix = '/customers/'
    def __init__(self, app):
        self.app = app
    
    @bind_to_app('get', 'all/')
    async def get_customers(self):
        pass

    @bind_to_app('get', 'filtered/')
    async def get_customers_with_product(self):
        pass