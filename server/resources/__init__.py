from .create import create_db_resources
from config import db
from sqlalchemy import Boolean

creds = {
    # база данных
    'test': {
        "hostname": db.hostname,
        "username": db.username,
        "password": db.password,
        "schema": "main"
    },
}
engines, tables, inspectors = create_db_resources(creds)
print(list(tables.keys()))
print(list(tables['test'].keys()))
