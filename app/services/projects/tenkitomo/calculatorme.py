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