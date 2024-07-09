from pydantic import BaseModel, class_validators


class Message(BaseModel):
    message: str

