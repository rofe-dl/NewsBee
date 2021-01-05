from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from . import validator

login_html_dir = "user_auth/login.html"
register_html_dir =  "user_auth/register.html"

def get_countries():
    country_codes = dict()
    with open("countries.txt") as f:
        for line in f:
            current_line = line.strip().split(':')
            country_codes[current_line[0]] = current_line[1]

    return country_codes
    
country_codes = get_countries()

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))

    return HttpResponseRedirect(reverse("mainapp:news"))

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user_auth:index"))
        else:
            return render(request, login_html_dir, {
                "message" : "Username or Password is incorrect",
                "username" : username
            })

    elif request.user.is_authenticated:
        return HttpResponseRedirect(reverse("mainapp:news"))

    return render(request, login_html_dir)

def logout_view(request):
    logout(request)
    return render(request, login_html_dir)

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        country = request.POST["country"]

        if not email.strip() or not full_name.strip() or not username.strip(): #empty fields
            return render(request, register_html_dir, {
            "message" : "Kindly fill up all the fields",
            "countries" : country_codes.keys()
        })

        elif validator.user_exists(request, username):
            return render(request, register_html_dir, {
                "message" : "Username not available",
                "countries" : country_codes.keys()
            })

        elif validator.test_password(request, password):
            return render(request, register_html_dir, {
            "message" : "Your password is not strong enough",
            "countries" : country_codes.keys()
        })

        elif validator.confirm_password(request, password, confirm_password):
            return render(request, register_html_dir, {
            "message" : "Your passwords do not match",
            "countries" : country_codes.keys()
        })

        

        user = User.objects.create_user(username, email, password)
        user.first_name = full_name
        
        user_profile = UserProfile()
        user_profile.country = country_codes[country]
        user_profile.user = user

        user.save()
        user_profile.save()

        return HttpResponseRedirect(reverse("user_auth:login"))

    elif request.user.is_authenticated:
        return HttpResponseRedirect(reverse("mainapp:news"))

    return render(request, register_html_dir, {
        "countries" : country_codes.keys()
    })

