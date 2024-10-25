from django.shortcuts import render,redirect
from .models import WeatherData, DailyWeatherSummary, Alert
from django.http import JsonResponse
from .fetch_weather import fetch_weather_data  # Import your data fetching function
from django.conf import settings
from django.utils import timezone
import requests
import logging
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)


def home(request):
    # Fetch the latest weather data to display on the home page
    latest_weather = WeatherData.objects.order_by('-timestamp')[:6]# Get latest 5 records
    return render(request, 'index.html', {'latest_weather': latest_weather})


def alerts(request):
    # Fetch all alerts to display on the alerts page
    all_alerts = Alert.objects.order_by('-timestamp')  # Get alerts ordered by timestamp
    return render(request, 'alerts.html', {'alerts': all_alerts})

def search(request):
    return render(request, 'search.html')


def get_weather(request):
    city = request.POST.get('city')
    if not city:
        return render(request, 'search.html',{'error': 'City cannot be empty'})

    api_key = settings.OPENWEATHER_API_KEY  # Ensure your API key is stored in settings.py
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return render(request, 'search.html', {'weather_data': weather_data, 'city': city})
    else:
        return render(request, 'search.html', {'error': 'City not found'})

def trigger_fetch_weather(request):
    logger.info("Manual fetch triggered.")
    fetch_weather_data()  # Manually fetch the weather data
    return JsonResponse({"message": "Weather data fetched successfully."})

def create_alert(request):
    city = request.POST.get('city')
    temperature = request.POST.get('temperature')
    email = request.POST.get('email')

    if city and temperature and email:
        alert = Alert.objects.create(city=city, temperature=temperature, email=email, timestamp=timezone.now())
        all_alerts = Alert.objects.order_by('-timestamp')  # Get alerts ordered by timestamp
        return render(request, 'alerts.html', {'alerts': all_alerts})
    return JsonResponse({'error': 'Invalid data.'}, status=400)

 # Change this to POST
def delete_alert(request, alert_id):
    print("Deleting alert", alert_id)
    try:
        alert = Alert.objects.get(id=alert_id)
        alert.delete()
        return redirect('alerts')  # Redirect to the alerts page after deletion
    except Alert.DoesNotExist:
        return JsonResponse({'error': 'Alert not found.'}, status=404)