from fastapi import FastAPI, HTTPException, Request, APIRouter
from pydantic import BaseModel

from routes import setup_routes

app = FastAPI()

setup_routes(app)
