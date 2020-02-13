import requests
import jwt
import uuid

def get_jwt_access_token(usernameFromInput, passwordFromInput):

    data = {
        'username': usernameFromInput,
        'password': passwordFromInput,
    }

    #secret = str(uuid.uuid4())
    secret = 'secret'

    #response = requests.post('https://website.com/get/token', data=data, verify=False).json()
    access_token = jwt.encode(data, secret, algorithm='HS256')

    response = access_token.decode()

    return response
