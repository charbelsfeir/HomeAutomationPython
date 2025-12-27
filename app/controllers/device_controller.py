from fastapi import APIRouter, UploadFile, Request, File, Form, HTTPException, Depends
from app.schemas.device import Device
router = APIRouter()


@router.get('/trigger-alarm')
async def trigger_alarm(device: Device):
    pass
