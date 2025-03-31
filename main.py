import streamlit as st
import pickle
import pandas as pd
import requests
import time

# Set the page configuration
st.set_page_config(
    page_title="Movie Recommender System 🎥",  # Title for the browser tab
    page_icon="🎬",  # Icon for the browser tab (can be an emoji or a URL to an image)
)

def fetch_poster(movie_id):
    """Fetch the movie poster using TMDb API with retry logic."""
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=669f4bc3eee5a0953b3f453b89654e11&language=en-US'
    for attempt in range(3):  # Retry up to 3 times
        try:
            response = requests.get(url, timeout=5)  # Set a timeout for the request
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()
            if 'poster_path' in data and data['poster_path']:
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            else:
                return "https://via.placeholder.com/500x750?text=No+Image"
        except requests.exceptions.RequestException as e:
            if attempt < 2:  # Retry for the first 2 attempts
                time.sleep(3)  # Wait before retrying
                continue
            # Log the error and return a placeholder image
            st.warning(f"⚠️ Error fetching poster for movie ID {movie_id}: {e}")
            return "https://via.placeholder.com/500x750?text=No+Image"
    

def recomend(movie):
    """Recommend movies based on similarity."""
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distance = similarity[movie_index]
        movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        recommended_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id  # Ensure 'movie_id' exists in your dataset
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_posters
    except Exception as e:
        st.error(f"⚠️ Error in recommendation: {e}")
        return [], []

# Load the movie data and similarity matrix
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('MOVIE RECOMMENDER SYSTEM 🎥')

selected_movie_name = st.selectbox(
    'Choose a movie', movies['title'].values
)

if st.button('Recommend'):
    names, posters = recomend(selected_movie_name)
    cols = st.columns(3)  # Create 3 columns for displaying recommendations
    for idx, col in enumerate(cols):
        with col:
            if idx < len(names):  # Ensure no index out of range error
                st.text(names[idx])
                st.image(posters[idx], use_container_width=True)