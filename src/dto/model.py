from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    name: str
    api: str
    token_bot: str
    is_active: bool


class Tasks(BaseModel):
    name: str
    description: str
    data_start: date
    data_end: date


