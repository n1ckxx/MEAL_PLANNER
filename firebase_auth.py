import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

def sign_up(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return user
    except Exception as e:
        return str(e)

def sign_in(email, password):
    # Firebase Admin SDK does not support direct user sign-in
    # You might need to use Firebase client SDK in your front end
    pass
