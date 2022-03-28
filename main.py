import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./serviceAccountKey.json")
link = "https://teste-firebase-17f6a-default-rtdb.firebaseio.com/"

firebase_admin.initialize_app(cred, {'databaseURL': link})

