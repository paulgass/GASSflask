import jwt
import uuid
import os
import logging
from functools import wraps
from flask import request, abort
from app.exception import (
    InvalidHttpHeaderException,
    InvalidTokenException,
    EnvironmentVariableNotFoundException
)

logger = logging.getLogger('authentication')

def log_request(decoded_token):
    values = {}
    # request user ip
    client_ip = request.remote_addr
    values['clientip'] = client_ip
    # username from token
    username = decoded_token['preferred_username']
    values['user'] = username
    r = request

    logger.info(
        'calling %s for endpoint %s with HTTP Headers: %s',
        request.method,
        request.path,
        request.headers.environ,
        extra=values
    )

def get_encoded_token_from_header():
    auth_header = request.environ.get('HTTP_AUTHORIZATION')

    if not auth_header:
        raise InvalidHttpHeaderException('Authorization header missing from request.')
    # split the value ( first should be Bearer and second should be the token )
    values = auth_header.split()

    if len(values) != 2:
        raise InvalidHttpHeaderException('Authorization header should be in format "Bearer <token>"')

    return values[1]

def get_public_key_from_env():
    # public key
    value = os.getenv('SSO_PUBLIC_KEY')

    if not value:
        raise EnvironmentVariableNotFoundException('No environment variable found for SSO_PUBLIC_KEY')

    return value

def validate_encoded_token(encoded_token):
    public_key = 'secret'
    #public_key = get_public_key_from_env()

    try:
        decoded_token = jwt.decode(encoded_token, public_key, algorithms='HS256')
    except Exception as e:
        raise InvalidTokenException('token provided is invalid: ' + str(e))

    return decoded_token

def verify_jwt_in_request():
    # check if auth should be checked
    skip_authentication = os.getenv('SKIP_AUTH', 'False')

    if skip_authentication.upper() == 'TRUE':
        return None
    # get token from request header
    encoded_token = get_encoded_token_from_header()
    # validate token
    decoded_token = validate_encoded_token(encoded_token)
    # log request
    #log_request(decoded_token)

    return decoded_token

def authenticate(fn):
    """
    A decorator to protect a Flask endpoint.
    If you decorate an endpoint with this, it will ensure that the requester
    has a valid access token before allowing the endpoint to be called. This
    does not check the freshness of the access token.
    See also: :func:
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception as e:
            message = 'could not verify access token'
            if e.args[0] is not None:
                message = e.args[0]
            abort(401, message)
        return fn(*args, **kwargs)
    return wrapper
