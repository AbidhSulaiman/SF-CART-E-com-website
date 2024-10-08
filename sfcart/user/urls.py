from django.urls import path
from .views import user_login

app_name = 'user'

urlpatterns = [
    path('user_login/',user_login, name = 'user_login'),
]