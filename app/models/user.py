from pydantic import BaseModel
from typing import List
from app.schemas.device import Device


class User(BaseModel):
    devices: List[Device]
