import json
import requests
from pprint import pprint

API_KEY = ''
URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko'

genre_json = requests.get(URL).json()

genres = []

for genre in genre_json['genres']:
    genre_data = {}
    genre_data['model'] = 'movies.genre'
    genre_data['pk'] = genre.get('id')
    genre_data['fields'] = {
        'name': genre.get('name')
    }
    genres.append(genre_data)

#pprint(genres)

with open('genre.json', 'w', encoding='utf-8') as f:
    json.dump(genres, f, ensure_ascii=False, indent='\t')