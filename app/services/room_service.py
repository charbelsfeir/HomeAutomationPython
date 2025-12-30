from app.schemas.room import Room
from app.core.firebase_init import db
from app.services.device_service import delete_device_room

# def process_registration(device_to_register: Device, user_email: str):
#     if user_email is not None and device_to_register.userEmail != user_email:
#         db.collection('users').document(user_email.lower()).collection(
#             'devices').document(device_to_register.id).delete()
#     db.collection('users').document(
#         device_to_register.userEmail.lower()).set({})
#     # db.collection('users').document(device_to_register.userEmail).set({})
#     db.collection('users').document(device_to_register.userEmail.lower()).collection('devices').document(
#         device_to_register.id).set(device_to_register.model_dump())


def update_room(room: Room):
    db.collection('users').document(room.userEmail.lower()).collection('rooms').document(room.id).update({
        'name': room.name
    })
    # query = db.collection_group("devices")
    # devices = query.stream()
    # device_found = None
    # for dev in devices:
    #     if device.id == dev.id:
    #         device_found = dev
    #         break
    # if device_found is None:
    #     user_email = None
    # else:
    #     user_email = device_found.reference.parent.parent.id
    #     device_found = Device(
    #         id=device_found.id, name=device_found.get('name'), userEmail=device.userEmail)
    # # user_email = (
    #     # device if device_found is None else device_found).reference.parent.parent.id
    # process_registration(
    #     device if device_found is None else device_found, user_email)


def delete_room(room: Room):
    delete_device_room(room)
    db.collection('users').document(room.userEmail.lower()
                                    ).collection('rooms').document(room.id).delete()
    # query = db.collection_group("devices")
    # devices = query.stream()
    # device_found = None
    # for dev in devices:
    #     if device.id == dev.id:
    #         device_found = dev
    #         break
    # if device_found is None:
    #     user_email = None
    # else:
    #     user_email = device_found.reference.parent.parent.id
    #     device_found = Device(
    #         id=device_found.id, name=device_found.get('name'), userEmail=device.userEmail)
    # # user_email = (
    #     # device if device_found is None else device_found).reference.parent.parent.id
    # process_registration(
    #     device if device_found is None else device_found, user_email)
