from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import public_ip as ip
import geocoder
import python_weather
from asgiref.sync import async_to_sync


class HelloView(APIView):
    @async_to_sync
    async def get(self, request):
        # Extract visitor_name from request
        visitor_name = request.GET.get('visitor_name', "").strip('()').strip('"') or 'World'

        # Get the client's public IP address
        client_ip = ip.get()
        
        # Get the client's location based on the IP address
        client_location = geocoder.ip(client_ip)

        # Define the async function to get the weather
        async def get_weather(city):
            async with python_weather.Client() as client:
                weather = await client.get(city)
                return weather

        # Run the async function to get the weather
        weather_data = await get_weather(client_location.city)

        # Prepare the response data
        response_data = {
            'client_ip': client_ip,
            'location': client_location.city,
            "greeting": f"Hello, {visitor_name}!, the temperature is {weather_data.temperature} degrees Celcius in {client_location.city}"
        }

        return JsonResponse(response_data)
