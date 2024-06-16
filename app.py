from flask import Flask, render_template, request
import requests
from datetime import datetime
import math
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # api key is how you access the data
    api_key = 'ea68e3d3ed994ec7a7f8dc81ae326d84'
    # get the city if not there then use adelaide
    city = request.args.get('city')
    if city is None:
        city = 'adelaide'
    # make the request
    url = "https://api.openweathermap.org/data/2.5/forecast?q=" + city +"&APPID="+api_key
    print(url)
    response = requests.get(url).json()
    # parse the response
    city_name = response["city"]["name"]
    forecast_list = response['list']
    forecast_data = []
    index = 0
    while index < len(forecast_list):
        dt_txt = forecast_list[index]['dt_txt']
        temp = forecast_list[index]['main']['temp']
        icon = forecast_list[index]['weather'][0]['icon']
        desc = forecast_list[index]['weather'][0]['description']
        date_object = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        day_name = date_object.strftime('%A')
        print(day_name)
        dict = {
            "dt_txt":dt_txt,
            "day_name":day_name,
            "temp":math.floor(int(temp)-273),
            "icon_url":"http://openweathermap.org/img/w/" + icon + ".png",
            "desc":desc
        }
        forecast_data.append(dict)
        index += 8
    print(forecast_data)
    # return the rendered html, passing in the data
    return render_template('home.html', forecast_data=forecast_data, city_name=city_name)


if __name__ == '__main__':
    app.run(debug=True)