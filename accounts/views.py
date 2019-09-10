from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from voteshop.helpers import calculate_cost


# Account app login and logout views

@login_required
def logout(request):
    """Logs out a user"""
    auth.logout(request)
    messages.success(request, "Successfully logged out!")
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

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome!")

                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


# Registration views


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
                messages.success(request, "Successfully registered a new user!")
            else:
                messages.error(request, "Couldn't register you, try again later : (")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


# User profile views, with order list display and pagination


def user_profile(request):
    """Returns user profile"""
    user = request.user
    orders_list = user.order_set.order_by('-created').all()
    paginator = Paginator(orders_list, 5)
    page = request.GET.get('page')
    page = page if page is not None else '1'

    return render(request, 'profile.html', {"user": user, "orders": paginator.page(page)})
