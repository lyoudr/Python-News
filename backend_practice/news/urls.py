from django.urls import path
from . import views

urlpatterns = [
    path('loginpage/', views.login_view, name='login_view'),
    path('get_news/', views.get_news, name='get_news')
]
