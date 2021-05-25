from django.test import TestCase

import requests
# Create your tests here.


# http://openweathermap.org/img/wn/10d@2x.png [이미지 URL]
# https://openweathermap.org/weather-conditions [wheather 컬럼정보]
def get_weather():
    API_KEY = 'd57e371644d9902e233f378564a6257b'
    city_name = 'Seoul'
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

    res = requests.get(API_URL).json()
    weather = res['weather'][0]['main']
    img = res['weather'][0]['icon']
    IMG_URL = f'http://openweathermap.org/img/wn/{img}@2x.png'
    loc_name = res['name'] #도시명

    return weather, IMG_URL, loc_name

def recommend_movie():
    # print(f'___recommend_movie____')

    weather, IMG_URL, loc_name = get_weather() # wheather = ['Clear', 'Clouds', 'Rain', 'Tornado', '']
    # print('____서울시 위치 정보____')
    # print(weather,IMG_URL, loc_name)

    # 테스트코드 ( 날씨와 이미지 바꾸고 싶을 때 잠시 테스트용 코드 )
    # weather = 'Clear'
    # IMG_URL = 'http://openweathermap.org/img/wn/10n@2x.png'

    if weather == 'Thunderstorm':
        return ['공포', '범죄', '스릴러', '미스테리'], IMG_URL, loc_name
    elif weather == 'Drizzle':
        return ['드라마', '애니메이션', ], IMG_URL, loc_name
    elif weather == 'Rain':
        return ['로맨스', '음악', '애니메이션'], IMG_URL, loc_name
    elif weather == 'Snow':
        return ['판타지', '가족', 'SF'], IMG_URL, loc_name
    elif weather == 'Clear':
        return ['모험', '액션', '코미디'], IMG_URL, loc_name
    elif weather == 'Clouds':
        return ['TV 영화', '전쟁'], IMG_URL, loc_name
    else: # Atmosphere
        return ['역사', '서부', '다큐멘터리'], IMG_URL, loc_name

