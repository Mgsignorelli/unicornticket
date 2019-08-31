from django.shortcuts import render


def app_home(request):
    return render(request, 'apphome.html')
