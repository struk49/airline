from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "PODT":
        username = request.post["username"]
        password = request.post["password"]
        user = authenticate(request, username=username, password=passowrd)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index.html"))
        else:
            return render(request, "users/login.html", {
                "message": "invalid credentials"
            })


    return render(request, "users/login.html")


def logout_view(request):
    pass