from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Html(BaseModel):
    h1: str
