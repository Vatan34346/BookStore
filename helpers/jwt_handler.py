import time
import jwt
from helpers.env_helper import EnvironmentHandler


class JwtHandler:
    """develpoer: panteleimon gvichia"""
    def __init__(self):
        self.auth_secret = 'c352c2e9a15b2d67fb1591021fa1736ffc008404' \
            if EnvironmentHandler.get_env_variable('AUTH_SECRET') is None else EnvironmentHandler.get_env_variable('AUTH_SECRET')

        self.algorithm = 'HS256' \
            if EnvironmentHandler.get_env_variable('ALGORITHM') is None else EnvironmentHandler.get_env_variable('ALGORITHM')

        self.token = None

    def sign_jwt(self, userid):
        try:
            payload = {
                "userId": userid,
                "expiry": time.time() + 25000
            }

            self.token = jwt.encode(payload, self.auth_secret, algorithm=self.algorithm)

            return self.token
        except Exception as e:
            print('Error(JwtHandler) sign_jwt:', e)
            return {
                'error': f'{e}'
            }

    def decode__jwt(self, token):
        try:
            decode_token = jwt.decode(token, self.auth_secret, algorithms=self.algorithm)

            expiry = decode_token.get('expiry', 0)

            if expiry >= time.time():
                return decode_token
            else:
                return None

        except Exception as e:
            print('Error(JwtHandler) decode__jwt:', e)
            return {
                'error': f'{e}'
            }
