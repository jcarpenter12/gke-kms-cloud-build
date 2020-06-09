from flask import Flask
import os
import requests

# Constants
API_KEY = os.getenv("OW_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)


@app.route("/<city>")
def weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        r = requests.get(url).json().get("weather")[0].get("description")
        return str(r)
    except Exception as e:
        raise e
        return "API Call failed"


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
