from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from schemas import PostCreate, PostResponse

app = FastAPI()

post : list[dict]  = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },
    {
        "title": "title of post 2",
        "content": "content of post 2",
        "id": 2
    }
] 

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{post[0]['title']}</h1>"

@app.get("/api/post")
def get_post():
    return post