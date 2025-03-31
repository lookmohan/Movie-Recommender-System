
# 🎥 Movie Recommendation System

This is a **Movie Recommendation System** built using **Streamlit** and **Python**. It allows users to select a movie and get five similar movie recommendations based on a similarity score.

---

## 🚀 Features
- 🎯 Movie recommendations based on similarity.
- 🌐 Fetches movie posters from the TMDb API.
- 🛠️ Error handling with retry logic for reliable poster retrieval.
- 🖥️ User-friendly interface using **Streamlit**.

---

## 📂 Folder Structure
```
📁 Movie Recommendation System  
 ┣ 📁 Dataset  
 ┃ ┣ 📄 Movie recommendation sys.ipynb        # Data cleaning and model training notebook  
 ┃ ┣ 📄 tmdb_5000_credits.csv                 # Credits dataset  
 ┃ ┣ 📄 tmdb_5000_movies.csv                  # Movies dataset  
 ┣ 📁 MRS code  
 ┃ ┣ 📄 main.py                               # Streamlit app for recommendations  
 ┃ ┣ 📄 movies_dict.pkl                       # Pickle file for quick data access  
 ┃ ┣ 📄 similarity.pkl                        # Pickle file containing similarity matrix  
 ┃ ┣ 📄 README.md                             # Project documentation

```

---

## 🔥 Datasets Used
You can download the datasets from Kaggle:
- [TMDB 5000 Movies](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
- [TMDB 5000 Credits](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)

Once downloaded, place them inside the `Dataset` folder.

---

## 🛠️ Installation and Setup

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/your-username/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### ✅ 2. Install Dependencies
Make sure you have **Python 3.8+** installed. Install the required libraries:
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, use:
```bash
pip install streamlit pandas requests
```

### ✅ 3. Run the Application
To start the Streamlit app, use:
```bash
streamlit run main.py
```
Open your browser and navigate to `http://localhost:8501` to use the recommendation system.

---

## Sample Output
![main - Google Chrome 31-03-2025 16_47_58](https://github.com/user-attachments/assets/46343035-4f73-474a-b0b2-cc543e91e834)
![Movie Recommender System 🎥 - Google Chrome 31-03-2025 17_28_04](https://github.com/user-attachments/assets/013b19fc-3f38-4002-b12b-5f7846102d10)

---

## ⚙️ How It Works
1. **Data Cleaning and Model Creation:**  
   - The Jupyter Notebook in the `Dataset` folder preprocesses the movie data.
   - It creates the **similarity matrix** and saves it as `similarity.pkl`.  
   - The movie details are saved in `movies_dict.pkl` and `movies.pkl`.

2. **Recommender System Execution:**  
   - The **Streamlit app** loads the preprocessed data and similarity matrix.
   - It allows users to select a movie and displays five similar movies with their posters.

---

## 🛠️ API Key Usage
The project uses the **TMDb API** to fetch movie posters.  
If you want to replace the existing key with your own, modify this line in `main.py`:
```python
url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US'
```
Register at [TMDb](https://www.themoviedb.org/documentation/api) to get your own API key.

---

## 🔥 Contributions
If you wish to contribute:
- Fork the repo.
- Create a new branch.
- Make your changes and submit a pull request.

---

## 📄 License
This project is licensed under the **MIT License**.

---

✅ Happy recommending! 🎬
