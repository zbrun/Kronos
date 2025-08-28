from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/hw")
def read_root():
    return {"Hello": "World"}


@app.get("api/v1/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=3006)