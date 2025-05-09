
def validate_location(lat, lon):
    if lat is None or lon is None:
        return False, {"error": "Latitude and longitude are required."}
    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        return False, {"error": "Latitude and longitude must be numbers."}
    
    return True, None


def validate_weather_data(weather):
    if "error" in weather:
        return False, {"error": "Weather API failed", "details": weather["error"]}
    
    return True, None