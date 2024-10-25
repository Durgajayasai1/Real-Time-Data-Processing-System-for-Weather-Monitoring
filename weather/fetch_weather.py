import requests
from .models import WeatherData, Alert
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

def fetch_weather_data():
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    api_key = '887d3609656908972a346524d67cc852'  # Replace with your API key
    for city in cities:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
        if response.status_code == 200:
            data = response.json()
            weather = WeatherData(
                city=city,
                temperature=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                main_condition=data['weather'][0]['main'],
                timestamp=timezone.now()
            )
            weather.save()

            # Check for alerts
            check_alerts(weather)

def check_alerts(weather):
    # Fetch all alerts for the city
    alerts_for_city = Alert.objects.filter(city=weather.city)

    # Iterate through each alert and check if the threshold is exceeded
    for alert in alerts_for_city:
        threshold_temp = alert.temperature  # Threshold from the alert record

        # If the weather temperature exceeds the threshold, send the alert email
        if weather.temperature > threshold_temp:
            send_alert_email(alert)

def send_alert_email(alert):
    print("sending mail")
    subject = f'Weather Alert for {alert.city}'
    message = (f"Alert! The temperature in {alert.city} has exceeded the threshold.\n\n"
               f"Current Temperature: {alert.temperature}°C\n"
               f"Weather Condition: {alert.condition}\n\n"
               f"Stay safe!")
    recipient_list = [alert.email]  # Use the email from the alert record
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list,fail_silently=False)
