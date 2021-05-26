import json
import requests
from pprint import pprint

API_KEY = ''

movies = []

for page in range(1, 101):
    URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page={page}'
    movie_json = requests.get(URL).json()
    
    for movie in movie_json.get('results'):
        movie_data = {}
        movie_data['model'] = 'movies.movie'

        movie_id = movie.get('id')
        movie_data['pk'] = movie_id
        
        
        # video
        video_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=ko-KR'
        video_json = requests.get(video_URL).json()
        video = video_json.get('results')[0] if video_json.get('results') else {}

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


        movie_data['fields'] = {
            'title': movie.get('title'),
            'genres': movie.get('genre_ids'),
            'overview': movie.get('overview'),
            'poster_path': movie.get('poster_path'),
            'backdrop_path': movie.get('backdrop_path'),
            'release_date': movie.get('release_date'),
            'popular': movie.get('popularity'),
            'rating': movie.get('vote_average'),

            # trailer
            'trailer': video.get('key'),

            # Provider
            'netflix': netflix,
            'watcha': watcha,
            'wavve': wavve, 

            # custome data
            'pick_users': [],
            'wish_users': [],
            'watch_users': [],
            'dislike_users': [],
        }
        movies.append(movie_data)

#pprint(movies)
with open('movie.json', 'w', encoding='utf-8') as f:
    json.dump(movies, f, ensure_ascii=False, indent='\t')        