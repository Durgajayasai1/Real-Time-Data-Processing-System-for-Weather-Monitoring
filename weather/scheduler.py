from apscheduler.schedulers.background import BackgroundScheduler
from .fetch_weather import fetch_weather_data  # Import your fetch function


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_weather_data, 'interval', seconds=300)  # Fetch every 5 minutes
    scheduler.start()
