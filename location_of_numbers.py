import phonenumbers
from phonenumbers import geocoder ,carrier
import folium
from marker import Marker
from marker import *
print("_"*50)
enter_num=input("pleas enter u  num : ")
phone=phonenumbers.parse(enter_num)
print(phone)
#_________________________________________________________________
number_locatoin=geocoder.description_for_number(phone,"en")

serves_phone=phonenumbers.parse(enter_num)
print(carrier.name_for_number(serves_phone,"en"))
#print(timezone.time_zones_for_number(phone,"en"))
from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode('3567eb6762ae40649cb42ba4736bc130')
query=str(number_locatoin)
results=geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)
map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],Popup=phone).add_to(map_location)
map_location.save('mylocatoin.html')
