# GeoLocation-Distance
GeoLocation-Distance is a app that Calculate Distance and Show on the Map. The styling for the application is done using Bootstrap 4.5

##  Setup
Clone this project.

1. Move to the base directory: ```cd GeoLocation-Distance```

2. Create a new python enveronment with: ```virtualenv env```.

3. Activate enveronment with: ```env\Scripts\activate``` on windows, or ```source env/bin/activate``` on Mac and Linux.

4. Install required dependences with: ```pip install -r requirements.txt```.

5. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

6. Run app locally with: ```python manage.py runserver```.<br />
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view it in the browser.

## Files Have to Download
SignUp and Login -> [https://dev.maxmind.com/geoip/geoip2/geolite2/](https://dev.maxmind.com/geoip/geoip2/geolite2/) , Download Files -> 1) GeoLite2 City(Download GZIP) 2)GeoLite2 Country(Download GZIP).

Grab the files ```GeoLite2-City.mmdb``` from GeoLite2_City and ```GeoLite2-Country.mmdb``` from GeoLite2-Country move this files into ```geoip``` directory.

## Note
If your in MacOs GoTo Applications Find the Python Version you're using and run the ```install certificates.command```

## Certificate
This project is officialy certified by Jewells Joshi.
All rights reserved 2020.