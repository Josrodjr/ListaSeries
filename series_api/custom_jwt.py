from datetime import datetime
from calendar import timegm
from rest_framework_jwt.settings import api_settings

# Encriptar usando el token

def jwt_payload_handler(user):
  return {
    'user_id': user.pk,
    'email': user.email,
    'is_superuser': user.is_superuser,
    'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
    'orig_iat': timegm(
            datetime.utcnow().utctimetuple()
        )
  }

# Controlar el payload despues de login o refresh de token, mediante el API    

def jwt_response_payload_handler(token, user=None, request=None):
  return {
    'token': token,
    'user': {
      'user_id': user.pk,
      'username': user.username,
      'email': user.email,
      # 'password': user.password,
    }
  }