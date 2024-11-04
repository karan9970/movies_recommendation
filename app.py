from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches  # Import for handling close matches

# Load the saved TF-IDF vectorizer and matrix
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

with open('tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv', encoding='latin')
df = df.dropna(subset=['title', 'description', 'listed_in'])  # Ensure no nulls in key columns

# Recompute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Define the recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    # Check for close matches
    close_matches = get_close_matches(title, df['title'].str.lower().tolist())
    if not close_matches:
        return ["Movie not found. Please check the title or try a different one."]
    
    # Use the first close match
    title = close_matches[0]
    idx = df[df['title'].str.lower() == title].index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_indices = [i[0] for i in sim_scores[1:11]]
    
    return df['title'].iloc[sim_indices].tolist()

# Initialize Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    title = request.form['title']
    recommendations = get_recommendations(title)
    return render_template('index.html', recommendations=recommendations, title=title)

if __name__ == '__main__':
    app.run(debug=True)
