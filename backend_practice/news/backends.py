from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class CustomerBackend(ModelBackend):
  def authenticate(self, request, username=None, password=None):
    username = username
    password = password
    try:
      user_valid = User.objects.get(username=username)
      if user_valid:
        pwd_valid = check_password(password, user_valid.password)
        return user_valid
    except User.DoesNotExist:
      return False
  def get_user(self, user_id):
    try:
      return User.objectst.get(pk = user_id)
    except User.DoesNotExist:
      return None