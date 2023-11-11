from utils import set_attrs, sql_to_dict
from ._base_resource import Resource
from resources import engines, tables
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update, insert
from models import Product_model
from fastapi.encoders import jsonable_encoder


products = tables['test']['main.products']
customers = tables['test']['main.customers']
transactions = tables['test']['main.transactions']


class Product_resource(Resource):
    """class based on resource that allows to create scalable routes"""
    @set_attrs(method='post', route='create/', response_model=None)
    async def r_add_product(self, item: Product_model):
        """meth for add product, input Product_model"""
        with Session(engines['test']) as session:
            session.execute(insert(products).values(
                item.dict(exclude_unset=True)))
            session.commit()
            return None

    @set_attrs(method='patch', route='edit/{id}', response_model=Product_model)
    async def r_patch_product(self, id: int, item: Product_model):
        """meth for edit product, input int, Product_model"""
        with Session(engines['test']) as session:
            this_product = sql_to_dict(session, select(products.c).select_from(
                products).where(products.c.id == id))[0]
            this_product_typed = Product_model(**this_product)
            update_data = item.dict(exclude_unset=True)
            updated_item = this_product_typed.copy(update=update_data)
            session.execute(update(products).where(
                products.c.id == id).values(**jsonable_encoder(updated_item)))
            session.commit()
            return updated_item

    @set_attrs(method='delete', route='delete/{id}', response_model=None)
    async def r_delete_product(self, id: int):
        """meth for delete product, input int"""
        with Session(engines['test']) as session:
            session.execute(delete(products).where(products.c.id == id))
            session.commit()
            return None

    @set_attrs(method='get', route='all/', response_model=list[Product_model])
    async def r_get_products(self):
        """meth for get products"""
        with Session(engines['test']) as session:
            return sql_to_dict(session, select(products.c).select_from(products))

    @set_attrs(method='get', route='filtered/{customer_id}', response_model=list[Product_model])
    async def r_get_products_with_customer(self, customer_id: int):
        """meth for get filtered products, input int"""
        with Session(engines['test']) as session:
            return sql_to_dict(session,
                               select(
                                   products.c
                               ).select_from(
                                   products
                                   .join(transactions, products.c.id == transactions.c.idProduct, isouter=True)
                                   .join(customers, customers.c.id == transactions.c.idCustomer, isouter=True)
                               ).where(
                                   customers.c.id == customer_id
                               )
                               )
