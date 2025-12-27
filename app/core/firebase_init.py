import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore
cred = credentials.Certificate("app/core/firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
