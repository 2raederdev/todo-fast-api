import json
from typing import Any

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from model import Item


todo = APIRouter(prefix='/api/v1/todo')




@todo.post("/items", response_model=Item)
async def create_item(item: Item) -> Any:
    items = get_data()
    items.append(jsonable_encoder(item))
    write_data(items)
  
    return JSONResponse(content=jsonable_encoder(item), status_code=status.HTTP_201_CREATED)


@todo.put("/items/{title}")
async def update_item(title: str) -> Any:
    items = get_data()

    idx = await get_index(title, items)
    if idx < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    
    items[idx]['is_done'] = not items[idx]['is_done']
    write_data(items)

    return JSONResponse(content=jsonable_encoder(items[idx]), status_code=status.HTTP_200_OK)


@todo.delete("/items/{title}")
async def delete_item(title: str) -> Any:
    items = get_data()

    idx = await get_index(title, items)
    if idx < 0:
        raise HTTPException(status_code=404, detail="Item not found")

    items = [item for item in items if item['title'].lower().replace(" ","-") != title]
    write_data(items)

    return JSONResponse(content=jsonable_encoder(items), status_code=status.HTTP_200_OK)


@todo.get("/items", response_model=list[Item])
async def read_items() -> Any:
    items = get_data()

    return JSONResponse(content=jsonable_encoder(items), status_code=status.HTTP_200_OK)


async def get_index(title: str, items: list) -> int:
    for i, d in enumerate(items):
        if d['title'].lower().replace(" ","-") == title:
            return i
    return -1


def get_data():
    try:
        with open('items.json') as json_file:
            return json.load(json_file)
    except Exception as e:
        print(f'error: {e}')
        return JSONResponse(content=jsonable_encoder({'error': 'There was an error'}), status_code=status.HTTP_400_BAD_REQUEST)
    
def write_data(data):
    try:
        with open('items.json', 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        print(f'error: {e}')
        return JSONResponse(content=jsonable_encoder({'error': 'There was an error'}), status_code=status.HTTP_400_BAD_REQUEST)
