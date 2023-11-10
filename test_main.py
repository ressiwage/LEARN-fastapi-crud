from fastapi.testclient import TestClient
from models import Product_model
from fastapi.encoders import jsonable_encoder

from main import app

client = TestClient(app)

routes = """path                              full name
--------------------------------  ---------------------------------------------------------------
/customers/all/                   routes.customer.Customer_resource.r_get_customers
/customers/filtered/{product_id}  routes.customer.Customer_resource.r_get_customers_with_product
/docs                             fastapi.applications.FastAPI.setup.<locals>.swagger_ui_html
/docs/oauth2-redirect             fastapi.applications.FastAPI.setup.<locals>.swagger_ui_redirect
/openapi.json                     fastapi.applications.FastAPI.setup.<locals>.openapi
/products/all/                    routes.product.Product_resource.r_get_products
/products/create/                 routes.product.Product_resource.r_add_product
/products/delete/{id}             routes.product.Product_resource.r_delete_product
/products/edit/                   routes.product.Product_resource.r_patch_product
/products/filtered/{customer_id}  routes.product.Product_resource.r_get_products_with_customer
/redoc                            fastapi.applications.FastAPI.setup.<locals>.redoc_html"""

def test_get_customers():
    response = client.get("/customers/all/")
    assert response.status_code == 200

def test_get_products():
    response = client.get("/products/all/")
    assert response.status_code == 200

def test_get_filtered_clients():
    response = client.get("/customers/filtered/1")
    assert response.status_code == 200

def test_get_filtered_products():
    response = client.get("/products/filtered/1")
    assert response.status_code == 200

def test_create_delete():
    '''post and delete'''
    response = client.get("/products/all")
    start = response.json()['result']
    client.post("/products/create", json={'name':'testTestTest'})
    response = client.get("/products/all")
    end = response.json()['result']
    assert len(end)>len(start)
    target = [i['id'] for i in end if i['name'] == 'testTestTest']
    for t in target:
        client.delete(f"/products/delete/{t}")

def test_patch():
    '''create, patch, delete'''
    client.post("/products/create", json={'name':'testPatchtestPatchtestPatch'})
    start = client.get("/products/all").json()['result']
    target_ids = [i['id'] for i in start if i['name'] == 'testPatchtestPatchtestPatch']
    resp = client.patch(f"/products/edit/{target_ids[0]}", json={"idPhoto":1234})
    end = client.get("/products/all").json()['result']
    assert [i['idPhoto'] for i in end if i['id'] == target_ids[0]][0] == 1234
    for t in target_ids:
        client.delete(f"/products/delete/{t}")
