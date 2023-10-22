from django.shortcuts import render
import folium
from pages.models import buildingData


# Create your views here.
def home(request):
    buildings = buildingData.objects.all
    return render(request, "pages/home.html", {})