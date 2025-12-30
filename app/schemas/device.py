from pydantic import BaseModel
from app.schemas.alarm import Alarm
from typing import Optional, List


class Device(BaseModel):
    id: str
    name: str
    userEmail: str
    status: Optional[bool] = None
    power: Optional[int] = None
    current: Optional[float] = None
    type: Optional[str] = None
    room: Optional[str] = None
    alarms: Optional[List[Alarm]] = []
