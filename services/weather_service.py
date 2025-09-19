import requests

API_KEY = "399099fc1044b731f5d0201d3e73d438"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city"""
    url = f"{BASE_URL}?q={city},IN&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return {"error": data.get("message", "API error")}

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["main"],
        "wind_speed": data["wind"]["speed"],
        "clouds": data["clouds"]["all"]
    }

def general_weather_alerts(weather):
    alerts = []
    temp = weather["temperature"]
    humidity = weather["humidity"]
    condition = weather["condition"]
    wind_speed = weather["wind_speed"]

    # Temperature-based alerts
    if temp > 40:
        alerts.append("Heatwave conditions! Stay hydrated.")
    elif temp < 5:
        alerts.append("Cold wave alert! Protect sensitive crops and livestock.")

    # Humidity-based alerts
    if humidity > 80:
        alerts.append("High humidity, risk of fungal infections.")
    elif humidity < 20:
        alerts.append("Very dry conditions, monitor irrigation.")

    # Weather condition alerts
    if condition.lower() in ["rain", "drizzle", "thunderstorm"]:
        alerts.append("Heavy rain expected, ensure proper drainage.")
    elif condition.lower() in ["haze", "dust", "smoke"]:
        alerts.append("Poor visibility, avoid pesticide spraying.")

    # Wind alerts
    if wind_speed > 15:
        alerts.append("Strong winds may damage crops and trees.")

    return alerts

def crop_alert(weather):
    alerts = []
    temp = weather["temperature"]
    humidity = weather["humidity"]

    # Example crop-specific alerts (you can expand with more logic)
    if temp > 35 and humidity < 30:
        alerts.append("Risk of drought stress for sensitive crops.")
    if humidity > 80 and temp > 25:
        alerts.append("High risk of fungal diseases in crops.")
    
    return alerts
