import requests 
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()
CITY_DICT = {'Moscow':'lat=55.75&lon=37.61&',
             'Nwsk':'lat=54.01&lon=38.29&'}


def city_url(city, CITY_DICT=CITY_DICT):
    '''
    Функция формирует url под нужный город по значению из словаря 
    '''
    url = BASE_URL + CITY_DICT[city] + 'appid=' + API_KEY
    return url

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def weather_connector(url):
    '''
    Функция для подключения к API OpenWeather 
    '''
    response = requests.get(url).json()
    return response 

def weather_formater(response):
    '''
    Функция формирует сообщение для вывода погоды на экран 
    '''
    kelvin = response['main']['temp']
    feels_kelvin = response['main']['feels_like']
    humidity = response['main']['humidity']
    pressure = response['main']['pressure']
    wind_speed = response['wind']['speed']
    description = response['weather'][0]['description']
    time = dt.datetime.fromtimestamp(response['dt'] + response['timezone'])
    city = response['name']
    feels_temp = kelvin_to_celsius(feels_kelvin)
    temp = kelvin_to_celsius(kelvin)
    res = f"""
        =======================
        {city=}, дата - {time} \n
        Температура - {temp:.1f}°C
        Ощущается как - {feels_temp:.1f}°C
        Влажность - {humidity} 
        Давление - {pressure} 
        Скорость ветра - {wind_speed:.1f} 
        Описание - {description}
        =======================
    """
    return res

def weather(city='Moscow'):
    url = city_url(city)
    response = weather_connector(url)
    weather_message = weather_formater(response)
    return weather_message


if __name__ == '__main__':
    print(weather('Moscow'))