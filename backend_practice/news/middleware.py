from django.contrib.auth.models import User

class AuthenticateMiddleWare:
  def __init__(self, get_response):
    self.get_response = get_response

  def process_view(self, request, view_func, view_args, view_kwargs):
    if view_func.__name__ == 'login_view':
      return None
    user_id = request.META.get('HTTP_AUTHORIZATION')
    user = User.objects.get(pk = user_id)
    request.user = user

  def __call__(self, request):
    return self.get_response(request)