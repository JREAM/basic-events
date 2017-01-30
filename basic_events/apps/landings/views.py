from django.shortcuts import render


def home(request):
    """
    Home View
    """
    return render(request, 'home.html', {})

