from utils import set_attrs, sql_to_dict
from ._base_resource import Resource
from resources import  engines, tables
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update, insert
from models import Product_model
from fastapi.encoders import jsonable_encoder


products = tables['test']['main.products']
customers = tables['test']['main.customers']
transactions = tables['test']['main.transactions']




class Product_resource(Resource):    
    @set_attrs(method='post', route='create/')
    async def r_add_product(self, item:Product_model):
        with Session(engines['test']) as session:
            session.execute(insert(products).values(**jsonable_encoder(item)))
            session.commit()
            return {'code':200}

    @set_attrs(method='patch', route='edit/{id}')
    async def r_patch_product(self, id:int, item:Product_model):
        print(item)
        with Session(engines['test']) as session:
            this_product = sql_to_dict(session, select(products.c).select_from(products).where(products.c.id==id))[0]
            this_product_typed = Product_model(**this_product)
            update_data = item.dict(exclude_unset=True)
            updated_item = this_product_typed.copy(update=update_data)
            session.execute(update(products).where(products.c.id==id).values(**jsonable_encoder(updated_item)))
            session.commit()
            return {'code':200, 'item':updated_item}

    @set_attrs(method='delete', route='delete/{id}')
    async def r_delete_product(self, id:int):
        with Session(engines['test']) as session:
            session.execute(delete(products).where(products.c.id==id))
            session.commit()
            return {'code':200}

    @set_attrs(method='get', route='all/')
    async def r_get_products(self):
        with Session(engines['test']) as session:
            return {'result':sql_to_dict(session, select(products.c).select_from(products))}

    @set_attrs(method='get', route='filtered/{customer_id}')
    async def r_get_products_with_customer(self, customer_id:int):
        with Session(engines['test']) as session:
            return {'code':200, 'result':sql_to_dict(session, 
                select(
                products.c
                ).select_from(
                products
                .join(transactions, products.c.id==transactions.c.idProduct, isouter=True)
                .join(customers, customers.c.id==transactions.c.idCustomer, isouter=True)
                ).where(
                customers.c.id==customer_id
                )
                                         )}
