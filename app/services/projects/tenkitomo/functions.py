import os
import requests

def get_weather_data(lat,lon):
    # ### ### ###
    # Fetch current weather data from WeatherAPI using latitude and longitude.
    # ### ### ###

    URI = "https://api.weatherapi.com/v1/current.json"
    WEATHER_API_KEY= os.getenv("WEATHER_API_KEY")

    # Check if ID exist or can be read.
    if not WEATHER_API_KEY:
        raise ValueError("WEATHER_API_KEY not found in environment variables.")

    # Get Data
    try :
        response = requests.get(URI, params={
            "key": WEATHER_API_KEY,
            "q": f"{lat},{lon}"
        })

        response.raise_for_status()  # Raises HTTPError for bad responses (4xx/5xx)
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Weather API request failed: {e}")
        return {"error": str(e)}

