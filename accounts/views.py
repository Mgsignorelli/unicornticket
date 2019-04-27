from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

def index(request):
    """Returns index page"""
    return render(request,  'index.html')

@login_required
def logout(request):
    """Logs out a user"""
    auth.logout(request)
    messages.success(request, "You've successfully logged out!")
    return redirect(reverse('index'))

