from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home_00.html')

def search_movies(request):
    api_key = "d728ffd7"
    moods = request.GET.getlist('mood')  # Fetching multiple moods

    if not moods:
        moods = ['romantic']  # Default mood if none provided

    movies = []
    for mood in moods:
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={mood}&type=movie"
        response = requests.get(url)
        data = response.json()

        if data.get('Response') == 'True':
            movies.extend(data.get('Search', []))  # Adds the movies to the list

    unique_movies = {movie['imdbID']: movie for movie in movies}.values()
    return render(request, 'search_movies.html', {'movies': unique_movies, 'moods': moods})
