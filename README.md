# Movie Recommender System
A Django web application that recommends movies based on content similarity using TMDB 5000 dataset. Users enter a movie title to receive top 5 similar movie recommendations with posters fetched from TMDB API.​

## Features
Content-based movie recommendation using TF-IDF vectorization and cosine similarity

Bootstrap-powered responsive UI with dark theme

Real-time poster fetching from TMDB API

Pre-computed similarity matrix for fast recommendations

Handles 1494 movies from TMDB 5000 dataset​

## Tech Stack
Backend: Django, Python, Pandas, Pickle

ML: Scikit-learn (TF-IDF, Cosine Similarity)

Frontend: Bootstrap 5, HTML/CSS

API: TMDB (movie posters)

Dataset: TMDB 5000 movies + credits​

## Project Structure
text
.
├── Movie_Recommender_System.ipynb    
├── views.py                         
├── recommend.html                   
├── movies_dict.pkl                  
└── similarity.pkl                   
Quick Demo
text
Input: "Avatar"
Output: Jupiter Ascending, Apollo 18, Aliens vs Predator Requiem, etc.[file:1]
Setup Instructions
Prerequisites
Python 3.8+

Django 4.0+

Pandas, Scikit-learn, Requests

## 1. Clone & Setup
bash
pip install django pandas scikit-learn requests
django-admin startproject movie_recommender
cd movie_recommender
python manage.py startapp MovieRecommender
## 2. Generate Data Files
Run the Jupyter notebook Movie_Recommender_System.ipynb to create:

movies_dict.pkl - Cleaned movie data with tags

similarity.pkl - Cosine similarity matrix​

## 3. Configure Django
text
MovieRecommender/
├── views.py          
├── templates/
│   └── MovieRecommender/
│       └── recommend.html  
└── urls.py
settings.py (add):

python
INSTALLED_APPS += ['MovieRecommender']
TEMPLATES['DIRS'] += ['templates/']
4. URLs
movie_recommender/urls.py:

python
path('recommend/', MovieRecommender.views.recommend, name='recommend')
5. Run Server
bash
python manage.py runserver
Visit http://127.0.0.1:8000/recommend/
