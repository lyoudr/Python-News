import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from news.models import Category, News

# Create your views here.
# 1. LogIn
def login_view(request):
  req_info = json.loads(request.body)
  print('req_info is =>', req_info)
  username = req_info['username']
  password = req_info['password']
  user = authenticate(request, username=username, password=password)
  print('user is =>', user)
  print('model_to_dict is =>', model_to_dict(user))
  if user is not None:
    login(request, user)
    print('user.backend is =>', user.backend)
    return JsonResponse({'status': 'ok', 'user_id': user.id}, status = 200, safe=False)  
  else:
    raise ValidationError('Wrong user password or username')

# 2. Log Out
def logout_view(request):
  logout(request)

# 3. Get news of one category
@login_required 
# @permission_required('news.view_news', raise_exception = True)
def get_news(request):
  print('request.user is =>', request.user)
  print('user.is_authenticated is =>', request.user.is_authenticated)
  type_ca = request.GET['type']
  print('type_ca is =>', type_ca)
  category = Category.objects.get(type = type_ca)
  news = [ model_to_dict(news) for news in category.news_set.all() ]
  print('news is =>', news)
  return JsonResponse(news, status=200, safe=False)

