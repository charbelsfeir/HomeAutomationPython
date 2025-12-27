from pydantic import BaseModel
from datetime import datetime


class Alarm(BaseModel):
    id: str
    dateTime: datetime
    state: bool
