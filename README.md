# **Spotify Data Analysis and Recommendation System**

---

## **Overview**

This project analyzes Spotify listening data to uncover insights into personal listening habits and preferences. Additionally, it builds a personalized song recommendation system using audio features, culminating in an automated process to create a custom Spotify playlist.

The motivation for this project stemmed from dissatisfaction with Spotify's default recommendation system. This inspired the creation of a data-driven alternative, leveraging personal listening data and third-party datasets to provide tailored recommendations.

---

## **Features**

1. **Exploratory Data Analysis (EDA):**
   - Visualized listening trends over time (years, days, and hours).
   - Analyzed top tracks, artists, and genres based on listening time.
   - Measured listening diversity with metrics like the Gini Coefficient.

2. **Personalized Recommendations:**
   - Identified songs not previously listened to using cosine similarity on audio features.
   - Recommended tracks that align closely with personal listening preferences.

3. **Spotify Playlist Creation:**
   - Transformed recommendations into a Spotify playlist using the Spotify API.
   - Automated playlist creation directly from the recommendation output.

4. **Dataset Integration:**
   - Combined personal Spotify listening history with third-party datasets containing audio features and metadata.

5. **Data Cleaning and Transformation:**
   - Standardized and deduplicated track and artist names.
   - Handled missing values for consistent data analysis.

---

## **Dataset Sources**

1. **Personal Spotify Listening Data:**
   - Exported directly from Spotify via [Spotify Wrapped](https://www.spotify.com/us/wrapped/) or the [Spotify API](https://developer.spotify.com/documentation/web-api/).

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
  - Spotipy
  - TfidfVectorizer
  - Cosine Similarity
- **Tools:**
  - Google Colab
  - Kaggle Datasets

---

## **Project Workflow**

1. **Data Collection:**
   - Exported Spotify listening history and merged it with third-party datasets for additional audio features.

2. **Data Cleaning and Preprocessing:**
   - Handled missing values and standardized metadata.
   - Removed duplicate entries for accurate analysis.

3. **Exploratory Data Analysis:**
   - Visualized listening trends over time and evaluated diversity in preferences.
   - Explored the contribution of top tracks and artists to total listening time.

4. **Building the Recommendation System:**
   - Used cosine similarity on normalized audio features.
   - Recommended unlistened tracks closest in similarity to personal listening history.

5. **Playlist Creation:**
   - Automated the creation of a Spotify playlist from recommended tracks.
   - Used the Spotify API to search for tracks and add them to a playlist.

6. **Final Output:**
   - A CSV file (`personalized_recommendations.csv`) with recommended tracks.
   - A Spotify playlist reflecting the generated recommendations.

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

5. **Create a Spotify Playlist:**
   - Ensure you have your Spotify Developer credentials (client ID, client secret, and redirect URI).
   - Run the `create_spotify_playlist.py` script to generate a playlist from the recommendations:
     ```bash
     python create_spotify_playlist.py
     ```
   - Log in when prompted to authorize Spotify access.

6. **View Results:**
   - Explore the EDA visualizations and generated insights.
   - Enjoy your personalized Spotify playlist.

---

## **Outputs**

1. **Data Visualizations:**
   - Charts displaying top tracks, artists, and listening trends.
   - Gini Coefficient and cumulative percentage plots to evaluate listening diversity.

2. **Recommendations:**
   - A CSV file (`personalized_recommendations.csv`) containing 20 tracks personalized to your listening habits.

3. **Spotify Playlist:**
   - An automatically created playlist in your Spotify account, titled **"Personalized Playlist"**.

---

## **Future Work**

1. **Dynamic Playlists:**
   - Generate updated recommendations based on real-time listening data.

2. **Advanced Models:**
   - Investigate deep learning methods like neural collaborative filtering for more precise recommendations.

3. **Genre Analysis:**
   - Provide detailed genre-based insights and recommendations.

4. **User Clustering:**
   - Group users with similar listening patterns for collaborative recommendations.

---

## **Acknowledgments**

- Thanks to [Spotify](https://www.spotify.com) for inspiring this project.
- Gratitude to Kaggle contributors for providing detailed datasets.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.