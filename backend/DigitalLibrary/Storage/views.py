from django.shortcuts import render
from .models import Upload


def home(request):
    context = {
        'uploads': Upload.objects.all(),
    }
    return render(request, 'Storage/home.html', context)


def about(request):
    return render(request, 'Storage/about.html')
