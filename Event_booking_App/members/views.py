from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Registeration successful")
            return redirect("home")
    else:
        form = RegisterUserForm()
    return render(request, "register.html", {"form": form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect("login_user")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            # Redirect to a success page.
            return redirect("home")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Invalid login credentials")
            return redirect("login_user")

    else:
         return render(request, "login.html", {})


