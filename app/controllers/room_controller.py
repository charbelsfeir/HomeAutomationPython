from fastapi import APIRouter, UploadFile, Request, File, Form, HTTPException, Depends
from app.schemas.room import Room
from app.services.room_service import update_room, delete_room
from starlette.responses import JSONResponse

router = APIRouter(prefix='/room')


@router.put('/update', response_model=Room)
def register(room: Room):
    update_room(room)
    return JSONResponse(room.model_dump())


@router.delete('/delete', response_model=Room)
def register(room: Room):
    delete_room(room)
    return JSONResponse(room.model_dump())
