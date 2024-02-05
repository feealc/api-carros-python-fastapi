from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
from database.car_db import CarDb


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


app = FastAPI()


@app.get('/cars')
async def get_cars():
    db = CarDb()
    lines = db.select_all_cars()
    print(lines)
    return {'message': 'Hello World', 'data': lines}


# @app.get('/items/{item_id}')
# async def read_item(item_id):
#     return {'item_id': item_id}


# @app.get('/items/{item_id}')
# async def read_item(item_id: int):
#     return {'item_id': item_id}


# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}


# Because path operations are evaluated in order,
# you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:
# @app.get('/users/me')
# async def read_user_me():
#     return {'user_id': 'the current user'}


# @app.get('/users/{user_id}')
# async def read_user(user_id: str):
#     return {'user_id': user_id}
