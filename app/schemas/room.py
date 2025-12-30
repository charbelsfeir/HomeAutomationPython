from pydantic import BaseModel


class Room(BaseModel):
    id: str
    name: str
    userEmail: str
