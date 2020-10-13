from django.shortcuts import render
from .models import Image


def index(request):
    display_images = Image.all_images
    return render(request, 'index.html', {'display_images': display_images})


def search_by_category(request):
    if 'q' in request.GET and request.GET["q"]:
        search_term = request.GET.get("q")
        searched_images = Image.search_image_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {'searched_images': searched_images, 'message': message})


def filter_by_location(request, location_id):
    search_term = '1'
    searched_images = Image.filter_by_location(location_id)
    message = f"{search_term}"

    return render(request, 'search.html', {'searched_images': searched_images, 'message': message})
