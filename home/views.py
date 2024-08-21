from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.


def Index(request:HttpRequest):
    template = "index.html"
    if request.user.is_authenticated == True:
        print("autenticado")
        return render(request, template, {'is_auth': True})

    else:
        print("no autenticado")
        return render(request, template, {"is_auth": False})


def login_view(request:HttpRequest):
    template = "login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request=request, user=user, backend=None)
                return redirect('create')
                # return HttpResponsePermanentRedirect('/create')

            else:
                context = {
                    "form": LoginForm(),
                    "warning": "Datos incorrectos",
                    "is_auth": True,
                }
                return render(request, template, context)

    else:
        form = LoginForm()
        return render(request, template, {"form": form, "warning": ""})


def signup(request:HttpRequest):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data["confirm"]

            if password == confirm:
                new_user = User(username=username, password=make_password(password))
                new_user.save()
                return redirect('home')
                # return HttpResponsePermanentRedirect('/')
    else:
        form = SignupForm
        return render(request, "signup.html", {"form": form})


def signout(request:HttpRequest):
    if request.method == "POST":

        logout(request)
        return redirect('home')
        # return HttpResponsePermanentRedirect('/')
    
    else:
        return render(request, 'logout.html')
