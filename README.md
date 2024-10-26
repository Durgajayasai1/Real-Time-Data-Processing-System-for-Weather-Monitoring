# Weather Monitoring Alert System

A Django-based system that monitors weather conditions using the OpenWeatherMap API and sends alerts to users when temperatures exceed custom thresholds.

## Features

- **Weather Alerts**: Sends automated email alerts when the temperature in a selected city exceeds a user-defined threshold.
- **Multiple Alerts per City**: Supports multiple users and temperature thresholds for the same city.
- **Database-Powered Thresholds**: Dynamically retrieves temperature thresholds from the database for flexibility and control.
- **Automated Data Fetching**: Integrates with OpenWeatherMap to pull real-time weather data at set intervals using `APScheduler`.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/weather-monitoring-alert-system.git
cd weather-monitoring-alert-system

### 2. Install Dependencies

Make sure Python 3 and pip are installed, then install required packages:

```bash
pip install -r requirements.txt

