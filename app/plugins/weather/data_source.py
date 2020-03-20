import requests

async def get_weather_of_city(location: str) -> str:
  key = "dc7ba86799424ebeb8a37b302eff1577"
  r = requests.get("https://free-api.heweather.net/s6/weather/now",params={'location': location, 'key': key, 'lang': 'zh'})
  result = r.json()['HeWeather6'][0]
  if result['status'] == 'ok':
    now = result['now']
    return result['basic']['location'] + "的实时天气:\n天气状况: " + now['cond_txt'] + "\n体感温度: " + now['fl'] + "\n相对湿度: " + now['hum'] + "\n降水量: " + now['pcpn'] + "\n风向: " + now['wind_dir'] + "\n风速: " + now['wind_spd'] + "公里/小时\n风力: " + now['wind_sc'] + "级"
  else:
    return result['status']