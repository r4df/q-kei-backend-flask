import math

def calculate_dew_point(temp_c, humidity):
    # Magnus formula (simplified version)
    a = 17.27
    b = 237.7
    alpha = ((a * temp_c) / (b + temp_c)) + math.log(humidity / 100)
    dew_point = (b * alpha) / (a - alpha)
    return round(dew_point, 1)

def convert_wind_speed_kph_to_mps(wind_kph):
    # 36 kph = 10 m/s
    wind_speed_mps = wind_kph / 3.6
    return round(wind_speed_mps, 1)


# ┌────────────────────┬──────┬────────────┬────────────┬────────────┬────────────────────────────────────────┐
# │ Feature            │ Unit │ Good       │ Moderate   │ Bad        │ Notes                                  │
# ├────────────────────┼──────┼────────────┼────────────┼────────────┼────────────────────────────────────────┤
# │ Temperature        │ °C   │ ≥ 25       │ 15–24      │ < 15       │ Warmer is better                       │
# │ Humidity           │ %    │ ≤ 50       │ 51–70      │ > 70       │ Lower humidity = faster drying         │
# │ UV Index           │ -    │ ≥ 6        │ 3–5        │ < 3        │ UV helps kill bacteria & speeds drying │
# │ Cloud Cover        │ %    │ < 30       │ 30–70      │ > 70       │ Less cloud = more sunlight             │
# │ Wind Speed         │ m/s  │ ≥ 4        │ 2–3.9      │ < 2        │ Wind increases evaporation             │
# │ Dew Point          │ °C   │ < 10       │ 10–15      │ > 15       │ High dew = moist air, slow drying      │
# └────────────────────┴──────┴────────────┴────────────┴────────────┴────────────────────────────────────────┘
FEATURE_STS_DEFAULT = 0
FEATURE_STS_GOOD = 1
FEATURE_STS_MODERATE = 2
FEATURE_STS_BAD = 3

def classify_feature(value, feature):
    if feature == "temperature":
        if 18 <= value <= 28:
            return FEATURE_STS_GOOD
        elif 10 <= value < 18 or 28 < value <= 33:
            return FEATURE_STS_MODERATE
        else:
            return FEATURE_STS_BAD

    elif feature == "humidity":
        if 30 <= value <= 60:
            return FEATURE_STS_GOOD
        elif 20 <= value < 30 or 60 < value <= 75:
            return FEATURE_STS_MODERATE
        else:
            return FEATURE_STS_BAD

    elif feature == "uv_index":
        if value >= 6:
            return FEATURE_STS_GOOD
        elif 3 <= value < 6:
            return FEATURE_STS_MODERATE
        else:
            return FEATURE_STS_BAD

    elif feature == "cloud_cover":
        if value <= 20:
            return FEATURE_STS_GOOD
        elif value <= 50:
            return FEATURE_STS_MODERATE
        else:
            return FEATURE_STS_BAD

    elif feature == "wind_speed":
        if value >= 4:
            return FEATURE_STS_GOOD
        elif 2 <= value < 4:
            return FEATURE_STS_MODERATE
        else:
            return FEATURE_STS_BAD

    elif feature == "dew_point":
        if value < 10:
            return FEATURE_STS_GOOD
        elif 10 <= value <= 16:
            return FEATURE_STS_MODERATE
        else:
            return FEATURE_STS_BAD

    else:
        return FEATURE_STS_DEFAULT
