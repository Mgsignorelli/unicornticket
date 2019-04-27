from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm

def index(request):
    """Returns index page"""
    return render(request,  'index.html')

@login_required
def logout(request):
    """Logs out a user"""
    auth.logout(request)
    messages.success(request, "You've successfully logged out!")
    return redirect(reverse('index'))

def login(request):
    """Returns login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Renders registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You've successfully registered!")
            else:
                messages.error(request, "Couldn't register you, try again later : (")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
