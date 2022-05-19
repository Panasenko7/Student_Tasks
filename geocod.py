import requests

IPFY_URL = 'https://api.ipify.org/?format=json'
COUNTRY_URL = 'https://sys.airtel.lv/ip2country/{}/?full=true'
WEATHER_URL = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m'


def get_ip():
    response_dict = requests.get(IPFY_URL).json()
    my_ip = response_dict['ip']
    return my_ip


def get_coords_by_ip(ip):
    response_dict_country = requests.get(COUNTRY_URL.format(ip)).json()
    lat = response_dict_country['lat']
    lon = response_dict_country['lon']
    return lat, lon


def get_weather_by_coords(coords):
    response_dict_weather = requests.get(WEATHER_URL.format(coords[0],coords[1])).json()
    hourly_temp = response_dict_weather['hourly']['temperature_2m']
    return hourly_temp[::12]


ip = get_ip()
city_coords = get_coords_by_ip(ip)
city_weather = get_weather_by_coords(city_coords)


print(f"Your IP is:{ip}")
print(f"Coords of your city{city_coords}")
print(f"Weather prediction for next week morning/evening:{city_weather}")
