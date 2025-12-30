from fastapi import APIRouter, UploadFile, Request, File, Form, HTTPException, Depends
from app.schemas.device import Device
from app.services.device_service import register as register_device
from starlette.responses import JSONResponse

router = APIRouter(prefix='/device')


@router.get('/trigger-alarm')
async def trigger_alarm(device: Device):
    pass


@router.post('/register', response_model=Device)
def register(device: Device):
    register_device(device)
    return JSONResponse(device.model_dump())
