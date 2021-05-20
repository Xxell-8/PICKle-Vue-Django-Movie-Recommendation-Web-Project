import json
import requests
from pprint import pprint

API_KEY = ''

movies = []
# 500 페이지까지 있는데, 일단 10페이지까지만 받아볼게요.
for page in range(1, 6):
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page={page}'
    movie_json = requests.get(URL).json()
    
    for movie in movie_json.get('results'):
        movie_data = {}
        movie_data['model'] = 'movies.movie'

        movie_id = movie.get('id')
        movie_data['pk'] = movie_id

        # credit
        credit_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=ko'
        credit_json = requests.get(credit_URL).json()
        
        crews = credit_json.get('crew')
        director = ''
        for crew in crews:
            if crew['job'] == 'Director':
                director = crew.get('name')
                break
        
        # watch provider
        provider_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={API_KEY}'
        provider_json = requests.get(provider_URL).json()

        providers = provider_json.get('results', {}).get('KR', {}).get('flatrate', {})
        wavve = watcha = netflix = False
        for provider in providers:
            if provider.get('provider_id') == 356:
                wavve = True
            elif provider.get('provider_id') == 97:
                watcha = True
            elif provider.get('provider_id') == 8:
                netflix = True

        # detail
        detail_URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=ko-KR'
        detail_json = requests.get(detail_URL).json()
        country_data = detail_json.get('production_countries')
        country = country_data[0].get('name') if country_data else ''
        runtime = detail_json.get('runtime') or ''

        movie_data['fields'] = {
            'title': movie.get('title'),
            'overview': movie.get('overview'),
            'poster_path': movie.get('poster_path'),
            'backdrop_path': movie.get('backdrop_path'),
            'release_date': movie.get('release_date'),
            'genre_id': movie.get('genre_ids'),
            # credit
            'director': director,
            # Provider
            'netflix': netflix,
            'watcha': watcha,
            'wavve': wavve, 
            # details
            'country': country,
            'runtime': runtime,
        }
        movies.append(movie_data)

#pprint(movies)
with open('tmdb.json', 'a', encoding='utf-8') as f:
    json.dump(movies, f, ensure_ascii=False, indent='\t')        

