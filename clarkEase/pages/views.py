from django.shortcuts import render
import folium
import branca
from pages.models import buildingData
from django.template.loader import render_to_string
from django.http import JsonResponse



# Create your views here.
def home(request):
    buildings = buildingData.objects.all()
    
    # Creates a map. Alter coordinates and zoom based on location
    #mapCenter = [42.2516486,-71.8234353]
    min_lon, max_lon = -71.8276034, -71.8196882
    min_lat, max_lat = 42.2375396, 42.2579646
    
    map = folium.Map(max_bounds=True,
                     location=[42.2513208,-71.8233978],
                     zoom_start=17,
                     min_lat=min_lat,
                     max_lat=max_lat,
                     min_lon=min_lon,
                     max_lon=max_lon,
                     )
    
    # add a marker to the map for each building
    for building in buildings:
        coordinates = (building.latitude, building.longitude)
        popup_content = render_to_string('pages/marker_template.html', {'building': building})
        
        iframe = branca.element.IFrame(html=popup_content, width=196, height=360)
        popup = folium.Popup(iframe, max_width=500)
        folium.Marker(coordinates, popup=popup).add_to(map)
        #some of the coordinates that google maps gave me were a little off, but they are mostly where they should be
    
    return render(request, "pages/home.html", {'map':map._repr_html_()})

# I orginially had this really complex javascript thing here, and it would allow users to submits a broken elevator.
# I quickly learned that unless I had an actual HTTP server, this would not be possible and the command wouldnt work ):