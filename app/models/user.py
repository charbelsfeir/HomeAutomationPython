from pydantic import BaseModel
from typing import List, Optional
from app.schemas.device import Device


class User(BaseModel):
    devices: Optional[List[Device]]
    rooms: Optional[List[str]]
