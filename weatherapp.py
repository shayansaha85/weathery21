import requests

def getweather(city):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=79189ba1e5e8fd8ab2d64beb8073f4d9")
    d = response.json()
    t  = float(d["main"]["temp"]) - 273
    temparature = round(t, 2)
    return str(temparature) + "°C"

