from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import password_validation
from . import views

def user_exists(request, username):
    if User.objects.filter(username=username).exists():
        return True

def test_password(request, password):
    try:
        password_validation.validate_password(password)
    except:
        return True

def confirm_password(request, password, confirm_password):
    if password != confirm_password:
        return True