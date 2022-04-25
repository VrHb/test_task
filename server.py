from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import Response


app = FastAPI()

new_article = {
        42: {
            "name": "New_article",
            "body_article": "Some text here",
            "description": "some new article",
            "tags": [
                    "article",
                    "new"
                    ]
            }
        }

class Article(BaseModel):
    name: str
    body_article: str
    tags: set[str] = set()


@app.get("/")
async def simple_page():
    with open("template/index.html", "r") as file:
        page = file.read()
    response = Response(page, media_type="text/html")
    return response


@app.get("/articles/{article_id}")
async def getting_article(article_id: int):
    return new_article[article_id]


@app.post("/create_articles/{article_id}", response_model=Article, summary="Create an article")
async def create_article(article_id: int, article: Article):
    new_article[article_id] = {
            "name": article.name, "body_article": article.body_article,
            "tags": article.tags
            }
    return new_article[article_id]
