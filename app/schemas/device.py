from pydantic import BaseModel
from app.schemas.alarm import Alarm
from typing import Optional, List


class Device(BaseModel):
    id: str
    name: str
    status: Optional[bool]
    power: Optional[int]
    current: Optional[float]
    type: Optional[str]
    room: Optional[str]
    alarms: List[Alarm]
