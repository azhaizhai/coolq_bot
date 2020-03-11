import requests

async def get_weather_of_city(location: str) -> str:
  key = "dc7ba86799424ebeb8a37b302eff1577"
  r = requests.get("https://free-api.heweather.net/s6/weather/now",params={'location': location, 'key': key, 'lang': 'zh'})
  result = r.json()['HeWeather6'][0]
  if result['status'] == 'ok':
    now = result['now']
    return result['basic']['location'] + "的实时天气:\n\t天气状况: " + now['cond_txt'] + "\n\t体感温度: " + now['fl'] + "\n\t相对湿度: " + now['hum'] + "\n\t降水量: " + now['pcpn'] + "\n\t风向: " + now['wind_dir'] + "\n\t风速: " + now['wind_spd'] + "公里/小时\n\t风力: " + now['wind_sc']
  else:
    return result['status']