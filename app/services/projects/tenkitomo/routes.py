from . import proj_tenkitomo_bp
from flask import jsonify, request
import joblib

from .functions import get_weather_data
from .validatorme import *
from .calculatorme import *

@proj_tenkitomo_bp.route("/test", methods=["POST"])
def r_test():
    return jsonify({"resp": "Tenkitomo test OK!"})

@proj_tenkitomo_bp.route("/predict", methods=["POST"])
def predict():
    
    try:

        # Load Models (Created through Machine Learning)
        drying_time_model = joblib.load('app/services/projects/tenkitomo/models/drying_time_model.pkl')
        recommendation_model = joblib.load('app/services/projects/tenkitomo/models/recommendation.pkl')

        # Frontend POST request
        user_data = request.get_json()
        lat = user_data.get("latitude")
        lon = user_data.get("longitude")
        is_valid, error_response = validate_location(lat, lon)
        if not is_valid:
            return jsonify(error_response), 400

        # Get/Validate weather data
        weather = get_weather_data(lat, lon)
        is_valid, error_response = validate_weather_data(weather)
        if not is_valid:
            return jsonify(error_response), 400

        # Calculate additional features (assuming these calculations happen here or elsewhere)
        uv = weather["current"]["uv"]
        cloud = weather["current"]["cloud"]
        temp_c = weather["current"]["temp_c"]
        humidity = weather["current"]["humidity"]
        dew_point = calculate_dew_point(temp_c, humidity)
        wind_speed = convert_wind_speed_kph_to_mps(weather["current"]["wind_kph"])

        # Prepare features
        weather_feat = [
            uv,
            cloud,
            humidity,
            temp_c,
            dew_point,
            wind_speed
        ]

        # Predict drying time
        drying_time = drying_time_model.predict([weather_feat])[0]

        # Recommendation model
        reco_feat = [
            drying_time,
            weather["current"]["uv"],
            weather["current"]["cloud"],
            humidity
        ]

        recommendation = recommendation_model.predict([reco_feat])[0]

        return jsonify({
            'drying_time_hours': round(drying_time, 2),
            'recommendation': bool(recommendation),
            'weather_feature': {
                "uv_index": uv,
                "cloud_cover": cloud,
                "humidity": humidity,
                "temperature": temp_c,
                "dew_point": dew_point,
                "wind_speed": wind_speed
            }
        }),200
    
    except Exception as e:
        return jsonify({
            'error': f"Error : {e}"
        }), 400