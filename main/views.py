from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import public_ip as ip
import ipinfo
import requests

OPENWEATHERMAP_API_KEY = '3399b556c2d716eb276740e0094f39c7'
access_token = 'a66a244ac36a36'
handler = ipinfo.getHandler(access_token)

class HelloView(APIView):
    
    def get(self, request):
        # Extract visitor_name from request
        visitor_name = request.GET.get('visitor_name', "").strip('()').strip('"') or 'World'

        # Get the client's public IP address
        client_ip = ip.get()
        
        # #for python anywhere only 
        # client_ip = request.META.get('HTTP_X_REAL_IP')

        
        # Get the client's location based on the IP address
        client_location = handler.getDetails(client_ip)
        city = client_location.city

        # Get weather data from OpenWeatherMap
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        # Extract temperature and weather description
        temperature = weather_data['main']['temp']

        # Prepare the response data
        response_data = {
                    'client_ip': client_ip,
                    'location': client_location.city,
                    "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {client_location.city}"
                }

        return JsonResponse(response_data)