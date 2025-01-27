# spotify-rec

---

# **Spotify Data Analysis and Recommendation System**

## **Overview**

This project analyzes Spotify listening data to uncover insights into personal listening habits and preferences. The project also builds a personalized song recommendation system using audio features, providing a custom playlist tailored to individual taste.

Spotify's default recommendation system inspired this project, but dissatisfaction with its suggestions led to the development of a data-driven alternative using personalized listening data combined with third-party datasets.

---

## **Features**

1. **Exploratory Data Analysis (EDA):**
   - Analyzed listening trends over time.
   - Visualized top tracks, artists, and genres by listening time.
   - Evaluated diversity in listening habits with metrics like Gini Coefficient.

2. **Personalized Recommendations:**
   - Identified songs not previously listened to using cosine similarity on audio features.
   - Recommended new tracks based on similarity to listening history.

3. **Dataset Integration:**
   - Combined Spotify listening history with third-party datasets containing detailed audio features and metadata.

4. **Interactive Visualizations:**
   - Provided insights using charts and plots to make data exploration intuitive.

5. **Data Cleaning and Transformation:**
   - Handled missing values and standardized data for consistency.
   - Deduplicated and normalized track names and artist names.

---

## **Dataset Sources**

1. **Personal Spotify Listening Data:**
   - Exported directly from Spotify (via [Spotify Wrapped](https://www.spotify.com/us/wrapped/) or [Spotify API](https://developer.spotify.com/documentation/web-api/)).

2. **Third-Party Datasets:**
   - [Spotify 12M Songs Dataset](https://www.kaggle.com/rodolfofigueroa/spotify-12m-songs)
   - [Spotify Tracks Genre Dataset](https://www.kaggle.com/thedevastator/spotify-tracks-genre-dataset)
   - [Spotify Audio Features Dataset](https://www.kaggle.com/tomigelo/spotify-audio-features)
   - [Spotify Dataset (1921-2020)](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-600k-tracks)

---

## **Technologies Used**

- **Programming Languages:**
  - Python
- **Libraries:**
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Scikit-learn
  - TfidfVectorizer
  - Cosine Similarity
- **Tools:**
  - Google Colab
  - Kaggle Datasets

---

## **Project Workflow**

1. **Data Collection:**
   - Exported Spotify listening history and integrated with third-party datasets for audio features.

2. **Data Cleaning and Preprocessing:**
   - Handled missing values and standardized metadata.
   - Merged multiple datasets and removed duplicates.

3. **Exploratory Data Analysis:**
   - Visualized listening trends over years, days, and hours.
   - Analyzed the contribution of top tracks and artists to total listening time.

4. **Building the Recommendation System:**
   - Used cosine similarity on normalized audio features.
   - Recommended unlistened tracks closest in similarity to listening history.

5. **Final Output:**
   - Created and saved a personalized playlist (`personalized_recommendations.csv`).
   - Delivered insights into listening preferences via visualizations and metrics.

---

## **Usage**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/spotify-data-analysis.git
   cd spotify-data-analysis
   ```

2. **Install Dependencies:**
   Install required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Project:**
   Execute the Jupyter Notebook or Python scripts in your preferred IDE or Google Colab.

4. **Input Your Data:**
   - Replace the example datasets with your Spotify listening data (CSV files).
   - Ensure your data follows the required format.

5. **View Results:**
   - Explore the EDA visualizations and generated insights.
   - Check your personalized song recommendations.

---

## **Outputs**

- **Data Visualizations:**
  - Charts displaying top tracks, artists, and listening trends.
  - Gini Coefficient and cumulative percentage plots showing diversity in listening habits.

- **Recommendations:**
  - A CSV file (`personalized_recommendations.csv`) containing 20 tracks personalized for you.

---

## **Future Work**

1. **Dynamic Playlists:**
   - Incorporate real-time updates to generate new recommendations based on evolving tastes.

2. **Advanced Models:**
   - Explore deep learning approaches like neural collaborative filtering for recommendations.

3. **Genre Analysis:**
   - Include detailed genre-based analysis and insights.

4. **User Clustering:**
   - Group similar users based on listening data for collaborative recommendations.

---

## **Acknowledgments**

- Thanks to [Spotify](https://www.spotify.com) for inspiring this project.
- Gratitude to the Kaggle contributors for providing detailed datasets.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
