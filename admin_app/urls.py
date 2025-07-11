from django.urls import path
from .views import admin_login_api

urlpatterns = [
    path('login/', admin_login_api, name='admin-login-api'),
]
