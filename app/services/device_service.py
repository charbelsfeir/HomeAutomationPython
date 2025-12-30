from app.schemas.device import Device
from app.schemas.room import Room
from app.core.firebase_init import db
from google.cloud import firestore


def process_registration(device_to_register: Device, user_email: str):
    if user_email is not None and device_to_register.userEmail != user_email:
        db.collection('users').document(user_email.lower()).collection(
            'devices').document(device_to_register.id).delete()
    db.collection('users').document(
        device_to_register.userEmail.lower()).set({})
    # db.collection('users').document(device_to_register.userEmail).set({})
    db.collection('users').document(device_to_register.userEmail.lower()).collection('devices').document(
        device_to_register.id).set(device_to_register.model_dump())


def register(device: Device):
    query = db.collection_group("devices")
    devices = query.stream()
    device_found = None
    for dev in devices:
        if device.id == dev.id:
            device_found = dev
            break
    if device_found is None:
        user_email = None
    else:
        user_email = device_found.reference.parent.parent.id
        device_found = Device(
            id=device_found.id, name=device_found.get('name'), userEmail=device.userEmail)
    # user_email = (
        # device if device_found is None else device_found).reference.parent.parent.id
    process_registration(
        device if device_found is None else device_found, user_email)


def update_device_by_field(field: str, value, device: Device):
    db.collection('users').document(device.userEmail.lower()).collection('devices').document(device.id).update({
        field: value
    })


def delete_device_room(room: Room):
    query = db.collection(f"users/{room.userEmail}/devices").where(
        filter=firestore.FieldFilter('room', '==', room.id))
    print(query.get(), room.id, room.userEmail)
    for device in query.get():
        update_device_by_field('room', None, Device(
            id=device.id, name='', userEmail=room.userEmail))
        # db.collection('users').document(room.userEmail).collection('devices').document(device.id)
