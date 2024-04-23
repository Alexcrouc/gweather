from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def search():
    global index
    api_key = 'ea68e3d3ed994ec7a7f8dc81ae326d84'
    city = 'adelaide'
    url = "https://api.openweathermap.org/data/2.5/forecast?q=" + city +"&APPID="+api_key
    print(url)
    response = requests.get(url).json()
    print("response:")
    print(response)
    city_name = response["city"]["name"]
    print(city_name)
    forecast_list = response['list']
    index = 0
    while index < len(forecast_list):
        print(forecast_list[index]['dt_txt'])
        print(forecast_list[index]['main']['temp'])
        print(forecast_list[index]['weather'][0]['icon'])
        print(forecast_list[index]['weather'][0]['main'])
        index += 8

    forecast_data = ""
    return render_template('home.html')


# @app.route('/results', methods=["GET", "POST"])
# def results():

    # city = response.get('city')
    # location = city.get('name')
    # timezone = city.get('timezone')
    # timestamp = city.get('dt')
    #
    # forecast_list = location_response["list"]
    # timestamp = forecast_list[0]['dt']
    # date_time = datetime.fromtimestamp(timestamp)
    # temp = forecast_list[0]['main']['temp']
    # description = forecast_list[0]['weather'][0]['description']
    # wind_speed = forecast_list[0]['wind']['speed']
    # first_time = datetime.fromtimestamp(forecast_list[0]['dt'])
    # daily_min = list([99] * 6)
    # daily_max = list([-99] * 6)
    # daily_name = list([''] * 6)
    # for forecast in forecast_list:
    #     dt = datetime.fromtimestamp(forecast['dt'])
    #     forecast['time'] = dt.strftime('%a %d %b, %I %p')
    #     day_number = dt.day - first_time.day
    #     forecast['daynumber'] = day_number
    #     temp_min = forecast['main']['temp_min']
    #     temp_max = forecast['main']['temp_max']
    #     daily_min[day_number] = min(daily_min[day_number], temp_min)
    #     daily_max[day_number] = max(daily_max[day_number], temp_max)
    #     daily_name[day_number] = dt.strftime('%a')
    # daily_data = zip(daily_name, daily_min, daily_max)
    # return render_template("home.html", data = location_response, daily_data = daily_data)

if __name__ == '__main__':
    app.run(debug=True)
