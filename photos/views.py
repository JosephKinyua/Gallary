from django.shortcuts import render
from .models import Image, Category, Location


# Create your views here.
def home(request):
    all_photos = Image.objects.all()
    all_category = Category.objects.all()
    all_location = Location.objects.all()

    if request.GET.get('location'):
        images = Image.filter_by_location(request.GET.get('location'))
        return render(request, 'all-photos/location.html', {'all_photos':images, 'all_category':all_category, 'locationn': request.GET.get('location')})
    return render(request, 'all-photos/home.html', {'all_photos':all_photos, 'all_category':all_category, 'all_location':all_location})


  

