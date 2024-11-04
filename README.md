# Movie Recommendation System

## Description

This Movie Recommendation System is a web application built using Flask, which recommends movies based on user input. The application utilizes the Netflix dataset to provide personalized recommendations. It implements a content-based filtering approach using TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity to find movies similar to the user's input.

To enhance user experience, the application incorporates fuzzy string matching, allowing users to receive recommendations even if they misspell the movie titles. This makes it easier to find movies based on partial or incorrect titles.

### Features

- Search for movie recommendations based on a given title.
- Fuzzy matching to handle misspelled or partially entered titles.
- Displays a list of recommended movies.

## Technologies Used

- Flask: A micro web framework for Python.
- Pandas: For data manipulation and analysis.
- Scikit-learn: For machine learning and cosine similarity calculations.
- Fuzzywuzzy: For fuzzy string matching to improve title recognition.

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
