from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    feels_like = models.FloatField()
    main_condition = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

class DailyWeatherSummary(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=100)
    avg_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    dominant_condition = models.CharField(max_length=100)

class Alert(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    email = models.EmailField()
