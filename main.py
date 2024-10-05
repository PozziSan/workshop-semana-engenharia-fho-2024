from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Hello World", "status": 200}


@app.get("/__health")
def health():
    return {200}


@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q, "status": 200}
