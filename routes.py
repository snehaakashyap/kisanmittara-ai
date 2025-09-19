from flask import Blueprint, render_template, request
from services.crop_service import recommend_crop

web_bp = Blueprint("web", __name__)

@web_bp.route("/")
def home():
    return render_template("home.html")

@web_bp.route("/services")
def services():
    return render_template("home.html")


@web_bp.route("/crop_form")
def crop_form():
    return render_template("crop_form.html")

@web_bp.route("/crop", methods=["POST"])
def crop_predict():
    N = float(request.form.get("N"))
    P = float(request.form.get("P"))
    K = float(request.form.get("K"))
    temperature = float(request.form.get("temperature"))
    humidity = float(request.form.get("humidity"))
    ph = float(request.form.get("ph"))
    rainfall = float(request.form.get("rainfall"))

    result = recommend_crop(N, P, K, temperature, humidity, ph, rainfall)

    return render_template("crop_result.html", 
                         crop_name=result,
                         N=N, P=P, K=K, 
                         temperature=temperature, 
                         humidity=humidity, 
                         ph=ph, 
                         rainfall=rainfall)


from services.fertilizer_service import recommend_fertilizer

@web_bp.route("/fertilizer_form")
def fertilizer_form():
    return render_template("fertilizer_form.html")

@web_bp.route("/fertilizer", methods=["POST"])
def fertilizer_predict():
    N = float(request.form.get("N"))
    P = float(request.form.get("P"))
    K = float(request.form.get("K"))

    result = recommend_fertilizer(N, P, K)

    return render_template("fertilizer_result.html", 
                         fertilizer_name=result,
                         N=N, P=P, K=K)


from services.weather_service import get_weather, crop_alert, general_weather_alerts

# Weather form page
@web_bp.route("/weather_form")
def weather_form():
    return render_template("weather_form.html")

# Handle form submission
@web_bp.route("/weather", methods=["POST"])
def weather_result():
    city = request.form.get("city")
    weather_data = get_weather(city)
    alerts = crop_alert(weather_data)
    general_alerts = general_weather_alerts(weather_data)

    return render_template("weather_result.html", city=city, weather=weather_data, alerts=alerts, general_alerts=general_alerts)


@web_bp.route("/flowise")
def flowise_chat():
    return render_template("flowise_chat.html")

@web_bp.route("/pest_disease")
def pest_disease():
    return render_template("pest_disease.html")

@web_bp.route("/test_form")
def test_form():
    return render_template("test_form.html")

@web_bp.route("/simple_crop_form")
def simple_crop_form():
    return render_template("simple_crop_form.html")

