from typing import Optional
from mangum import Mangum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    service_name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read():
    return {"aws_service": "Lambda",
            "lambda_handler": "Mangum",
            "asgi": "FastAPI"}


@app.post("/")
async def submit(item: Item):
    return {"service_name": item.service_name,
            "price": item.price,
            "offer": item.is_offer
            }


handler = Mangum(app)
