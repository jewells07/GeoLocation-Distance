from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address
import folium

# Create your views here.

def calculate_distance_view(request):
    # Intial Value
    distance = None
    destination = None

    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='measurements')

    # Get ip address or Manually at Below
    ip_ = get_ip_address(request)
    # print(ip_)

    # Manually -> Put Your Ip Address
    ip = '2405:205:c909:b8d0:5dc2:8025:59d1:bbbc'
    counrty, city, lat, lon = get_geo(ip)

    # print('location country', country)
    # print('location city', city)
    # print('location lat lon', lat, lon)
    location = geolocator.geocode(city)
    # print('###location',location)

    # Location Coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # Initial Folium Map
    m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)
    # Location marker
    folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'], icon=folium.Icon(color='purple')).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        # Destination Coordinates
        # print(destination)
        d_lat = destination.latitude
        d_lon = destination.longitude

        pointB = (d_lat, d_lon)

        # Distance Calculation
        distance = round(geodesic(pointA, pointB).km, 2)

        # Folium Map Modification
        m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon), zoom_start=get_zoom(distance))
        # Location marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'], icon=folium.Icon(color='purple')).add_to(m)
        # Destination marker
        folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=destination, icon=folium.Icon(color='red', icon='cloud')).add_to(m)


        # Draw The Line Between Location Destination
        line = folium.PolyLine(locations=[pointA, pointB], weigth=3, color='blue')
        m.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()
    
    # Override
    m = m._repr_html_()
    
    context = {
        'distance' : distance,
        'destination' : destination,
        'form' : form,
        'map' : m,
    }

    return render(request, 'measurements/main.html', context)