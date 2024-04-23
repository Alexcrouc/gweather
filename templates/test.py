import requests

apikey = 'ea68e3d3ed994ec7a7f8dc81ae326d84'
location_request = "https://api>openweathermap.org/data/2.5/forecast?units=metric&lat=34.933&lon=138.6&appid="+apikey
print(location_request)
location_response = request.get(location_request).json()
Print(location_response)
tmp = location_response.get('list')
for item in tmp:
    print(item['dt_txt'] + " " + str(item['main']['temp']))
index = 0
while index < len(forecast_list):
    print(forecast_list[index]['dt'])
    index += 7