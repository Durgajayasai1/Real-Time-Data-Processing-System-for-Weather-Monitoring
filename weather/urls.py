from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page to display weather data
    path('alerts/', views.alerts, name='alerts'),
    path('delete-alert/<int:alert_id>', views.delete_alert, name='delete_alert'),
    path('create-alert', views.create_alert, name='create_alert'),  # Page to display alerts
    path('fetch-weather/', views.trigger_fetch_weather, name='fetch_weather'),
    path('search/', views.search, name='search'),
    path('weather', views.get_weather, name='weather'),
]
