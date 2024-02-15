from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, ValidationError

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from routes.route import router

# переменная (название)
app = FastAPI()

app.include_router(router)

#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

