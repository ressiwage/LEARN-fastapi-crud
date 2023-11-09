def bind_to_app(method, url):
    '''first arg must be self, other args and kwargs are regular, at runtime fastapi ignores this argument'''
    def Inner(func):
        def wrapper(*args, **kwargs):
            app = args.pop(0).app
            if method=='post':
                app.post(url)(func(*args, **kwargs))
            elif method=='get':
                app.get(url)(func(*args, **kwargs))
            elif method=='patch':
                app.patch(url)(func(*args, **kwargs))
            elif method=='delete':
                app.delete(url)(func(*args, **kwargs))
            else:
                raise Exception('unknown method')
        return wrapper
    return Inner
 
