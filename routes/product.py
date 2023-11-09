from utils import bind_to_app
class Product_resource:
    _prefix = '/products/'

    
    @bind_to_app('post', 'add/')
    async def add_product():
        pass

    @bind_to_app('patch', 'edit/')
    async def patch_product():
        pass

    @bind_to_app('delete', 'delete/')
    async def delete_product():
        pass

    @bind_to_app('get', 'all/')
    async def get_products():
        pass

    @bind_to_app('get', 'filtered/')
    async def get_products_with_customer():
        pass