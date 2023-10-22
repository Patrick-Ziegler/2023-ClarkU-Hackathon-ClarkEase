from django.shortcuts import render
import folium
from pages.models import buildingData


# Create your views here.
def home(request):
    buildings = buildingData.objects.all()
    
    # Creates a map. Alter coordinates and zoom based on location
    #mapCenter = [42.2516486,-71.8234353]
    map = folium.Map(location=[42.2513208,-71.8233978], zoom_start=17)
    
    # add a marker to the map for each building
    for building in buildings:
        coordinates = (building.latitude, building.longitude)
        folium.Marker(coordinates).add_to(map)
    
    return render(request, "pages/home.html", {'map':map._repr_html_()})