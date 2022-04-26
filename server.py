from fastapi import FastAPI
from pydantic import BaseModel

from loguru import logger



app = FastAPI()

articles = {}

comments = {}

class Article(BaseModel):
    name_article: str
    body_article: str
    tags: set[str] = set()
    comments: dict | None = None


class Comment(BaseModel):
    comment_id: int
    user_id: int
    text: str
    comments: dict | None = None


@app.get("/articles/{article_id}")
async def getting_article(article_id: int):
    if article_id not in articles:
        return "Article not found!"
    return articles[article_id]


@app.post("/create_articles/{article_id}")
async def create_article(article_id: int, article: Article):
    articles[article_id] = article
    return articles[article_id]


@app.post("/articles/{article_id}/comments")
async def adding_comments(article_id: int, comment: Comment):
    comment_id = "C" + str(article_id)
    articles[article_id].comments = {comment_id: comment}
    return articles[article_id]


