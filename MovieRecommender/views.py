import os, pickle, requests
import pandas as pd
from django.conf import settings
from django.shortcuts import render

# Load movies and similarity
movies_path = os.path.join(settings.BASE_DIR, "movies_dict.pkl")
similarity_path = os.path.join(settings.BASE_DIR, "similarity.pkl")

movies_dict = pickle.load(open(movies_path, "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open(similarity_path, "rb"))

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")
    full_path = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "https://via.placeholder.com/500x750"
    return full_path

def recommend(request):
    recommendations = []
    movie_name = request.GET.get("movie")

    if movie_name and movie_name in movies['title'].values:
        movie_index = movies[movies['title'] == movie_name].index[0]
        distances = list(enumerate(similarity[movie_index]))
        top_movies = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]

        for i in top_movies:
            movie_id = movies.iloc[i[0]]['id']
            title = movies.iloc[i[0]]['title'] 
            poster = fetch_poster(movie_id)
            recommendations.append((title, poster))

    return render(request, "MovieRecommender/recommend.html", {"recommendations": recommendations})