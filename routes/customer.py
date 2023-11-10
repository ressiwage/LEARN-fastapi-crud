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

class Customer_resource(Resource):
    
    @set_attrs(method='get', route='all/')
    async def r_get_customers(self):
        with Session(engines['test']) as session:
            return sql_to_dict(session, select(customers.c).select_from(customers))
        
    @set_attrs(method='get', route='filtered/{product_id}')
    async def r_get_customers_with_product(self, product_id:int):
        with Session(engines['test']) as session:
            return {'code':200,'result':sql_to_dict(session, 
                select(
                customers.c
                ).select_from(
                customers
                .join(transactions, customers.c.id==transactions.c.idCustomer )
                ).where(
                transactions.c.idProduct==product_id
                )
                                         )}