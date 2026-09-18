import requests
import pandas as pd


API_URL = "https://historical-forecast-api.open-meteo.com/v1/forecast"

# Central Park, New York City
params = {
    "latitude": 40.7829,
    "longitude": -73.9654,
    "start_date": "2025-01-01",
    "end_date": "2025-01-07",
    "hourly": [
        "temperature_2m",
        "precipitation_probability",
        "precipitation",
        "rain",
    ],
    "timezone": "America/New_York",
    "models": "gfs_seamless",
}

response = requests.get(API_URL, params=params, timeout=30)

# Raise an error if the request was unsuccessful
response.raise_for_status()

data = response.json()

forecast = pd.DataFrame(data["hourly"])
forecast["time"] = pd.to_datetime(forecast["time"])

print(forecast.head())
print(f"\nDownloaded {len(forecast)} hourly forecasts.")