def set_attrs(**decor_kwargs):
    '''usage:
    @decorator_func(a=b,...)
    def inner(): ...
    inner.a'''
    def Inner(func):
        # def wrapper(*args, **kwargs):
        #     return func(*args, **kwargs)
        for i in decor_kwargs:
            setattr(func, i, decor_kwargs[i])
            # wrapper.b=x
        return func
    return Inner


def sql_to_dict(session, sql):
    return [row._mapping for row in session.execute(sql).all()]
