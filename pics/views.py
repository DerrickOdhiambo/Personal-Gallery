from django.shortcuts import render
from .models import Image


def index(request):
    display_images = Image.all_images
    return render(request, 'index.html', {'display_images': display_images})
