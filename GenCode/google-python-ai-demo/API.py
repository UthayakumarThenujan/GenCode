from fastapi import FastAPI
from pydantic import BaseModel
from CodeToHtml import *
from fastapi.middleware.cors import CORSMiddleware


class Topic(BaseModel):
    Topic: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

html = "<h1> No HTML</h1>"


@app.post("/topic")
async def postTopic(topic: Topic):
    response = mainDo(topic.Topic)
    global html
    html = response
    print(link)
    return html


@app.get("/link")
async def link():
    global link
    if link != False:
        return link
    else:
        return False


@app.get("/convert")
async def convert():
    global html
    return html
