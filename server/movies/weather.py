import requests


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

    weather, IMG_URL, loc_name = get_weather() 


    if weather == 'Thunderstorm':
        return ['공포', '범죄', '스릴러', '미스테리'], IMG_URL, loc_name
    elif weather == 'Drizzle':
        return ['드라마', '애니메이션', '다큐멘터리'], IMG_URL, loc_name
    elif weather == 'Rain':
        return ['로맨스', '음악', '애니메이션'], IMG_URL, loc_name
    elif weather == 'Snow':
        return ['모험', '판타지', '가족'], IMG_URL, loc_name
    elif weather == 'Clear':
        return ['액션', '코미디', '가족'], IMG_URL, loc_name
    elif weather == 'Clouds':
        return ['TV 영화', '전쟁'], IMG_URL, loc_name
    else: # Atmosphere()
        return ['역사', '서부', 'SF'], IMG_URL, loc_name

