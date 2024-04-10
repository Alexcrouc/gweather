from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def search():
    return render_template('home.html')


@app.route('/results', methods=["GET", "POST"])
def results():
    api_key = 'ea68e3d3ed994ec7a7f8dc81ae326d84'
    lon = 138.6  # Adelaide
    lat = -34.9333
    location = "https://api.openweathermap.org/data/2.5/forecast?units=metric&lat="+str(lat)+"&lon="+str(lon)+"&appid="+api_key
    location_response = requests.get(location).json()
    print("location_response:")
    print(location_response)
    
    city = location_response.get('city')
    location = city.get('name')
    timezone = city.get('timezone')
    timestamp = city.get('dt')

    forecast_list = location_response["list"]
    timestamp = forecast_list[0]['dt']
    date_time = datetime.fromtimestamp(timestamp)
    temp = forecast_list[0]['main']['temp']
    description = forecast_list[0]['weather'][0]['description']
    wind_speed = forecast_list[0]['wind']['speed']
    first_time = datetime.fromtimestamp(forecast_list[0]['dt'])
    for forecast in forecast_list:
        print(forecast['dt_txt'])
        dt = datetime.fromtimestamp(forecast['dt'])
        forecast['time'] = dt.strftime('%a %d %b, %I %p')
        forecast['daynumber'] = dt.day - first_time.day
        print(forecast['main']['temp_min'])
        print(forecast['main']['temp_max'])
    my_list = [location, timezone, timestamp, date_time, temp, description, wind_speed]
    print(my_list)

    # startdictionary
    weather_dict = {
        "location": location,
        "timezone": timezone,
        "wind_speed": wind_speed,
        "temp": temp,
        "timestamp": timestamp
    }
    return render_template("home.html", data = location_response, weather_data=my_list, weather_dict=weather_dict)

if __name__ == '__main__':
    app.run(debug=True)
