from inspect import signature

class Resource:
    """usage: init class with app, then setup(); routes adding by decor set_attrs and naming function as route_..."""

    def __init__(self, app, prefix):
        self.app = app
        self.prefix = prefix

    def local_bind(self, func, method, rel_url, response):
        '''first arg must be self, other args and kwargs are regular, at runtime fastapi ignores this argument'''
        url = self.prefix+rel_url
        if method == 'post':
            self.app.post(url, response_model = response)(func)
        elif method == 'get':
            self.app.get(url, response_model = response)(func)
        elif method == 'patch':
            self.app.patch(url, response_model = response)(func)
        elif method == 'delete':
            self.app.delete(url, response_model = response)(func)
        else:
            raise Exception('unknown method')

    def setup(self):
        """just call it and everything will be fine"""
        route_list = [func for func in dir(self) if callable(
            getattr(self, func)) and func.startswith("r_")]
        for route in route_list:
            route_fun = getattr(self, route)
            self.local_bind(route_fun, route_fun.method, route_fun.route, getattr(route_fun, 'response_model', None))
