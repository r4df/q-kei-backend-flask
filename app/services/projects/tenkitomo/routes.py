from . import proj_tenkitomo_bp
from flask import jsonify, request
import joblib

# Load models

drying_time_model = joblib.load('app/services/projects/tenkitomo/models/drying_time_model.pkl')
recommendation_model = joblib.load('app/services/projects/tenkitomo/models/recommendation.pkl')

@proj_tenkitomo_bp.route("/test", methods=["POST"])
def r_test():
    return jsonify({"resp": "Tenkitomo test OK!"})

@proj_tenkitomo_bp.route("/predict", methods=["POST"])
def predict():
    
    try:
        data = request.get_json()

        # Extract weather feature
        weather_feat = [
            data['uv_index'],
            data['cloud_cover'],
            data['humidity'],
            data['temperature'],
            data['dew_point'],
            data['wind_speed']
        ]

        # Predict drying time
        drying_time = drying_time_model.predict([weather_feat])[0]

        # Extract requirements for recommendation
        reco_feat = [
            drying_time,
            data['uv_index'],
            data['cloud_cover'],
            data['humidity']
        ]

        recommendation = recommendation_model.predict([reco_feat])[0]

        return jsonify({
            'drying_time_hours': round(drying_time, 2),
            'recommendation': bool(recommendation)
        }),200
    
    except Exception as e:
        return jsonify({
            'error': f"Error : {e}"
        }), 400