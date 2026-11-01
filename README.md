# Moodify AI – Emotion-Based Music Recommendation System

**Your emotions. Your music. Your mood.**

Moodify AI is an AI-powered music recommendation web application that detects facial emotions in real time and recommends songs based on the user's current mood.

The application combines computer vision, deep learning and web development to create a personalised music discovery experience.

## Features

- **Real-Time Emotion Detection:** Detects facial expressions using a webcam.
- **Emotion Recognition:** Identifies seven emotional states: Angry, Disgusted, Fearful, Happy, Neutral, Sad and Surprised.
- **Personalised Music Recommendations:** Suggests songs based on the detected emotion.
- **Spotify Integration:** Provides links to discover recommended tracks on Spotify.
- **Live Camera Interface:** Displays the webcam feed and detected emotion.
- **Dynamic Recommendations:** Updates recommendations when the detected emotion changes.
- **Interactive Dashboard:** Provides a user-friendly web interface.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| TensorFlow & Keras | Deep learning and emotion recognition |
| OpenCV | Face detection and image processing |
| Flask | Web application framework |
| NumPy & Pandas | Data processing |
| HTML, CSS & JavaScript | Frontend development |
| Spotipy / Spotify links | Music discovery |

## How It Works

1. The application accesses the user's webcam.
2. OpenCV detects the face in the video stream.
3. The facial image is processed and passed to the trained deep learning model.
4. The model predicts the user's current emotion.
5. The system selects songs from the corresponding emotion-based playlist.
6. Users can explore recommended songs through Spotify links.

## Supported Emotions

| Emotion | Recommendation Category |
|---|---|
| Angry | Angry |
| Disgusted | Disgusted |
| Fearful | Fearful |
| Happy | Happy |
| Neutral | Neutral |
| Sad | Sad |
| Surprised | Surprised |

## Project Structure

```text
Moodify-AI-Music-Recommendation/
│
├── songs/                  # Emotion-based music datasets
├── static/                 # CSS and frontend assets
├── templates/
│   └── index.html          # Main web interface
│
├── app.py                  # Flask application
├── camera.py               # Webcam and emotion detection
├── model.h5                # Trained emotion recognition model
├── haarcascade_frontalface_default.xml
├── train.py                # Model training
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Karann-404A/Moodify-AI-Music-Recommendation.git
```

### 2. Navigate to the project directory

```bash
cd Moodify-AI-Music-Recommendation
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

### 6. Open in your browser

Visit:

`http://127.0.0.1:5000/`

Allow webcam access when prompted.

## Application Preview

The application includes:

- Live facial emotion detection.
- Current mood display.
- Emotion-based recommended song cards.
- Spotify music discovery links.
- An interactive music recommendation dashboard.

## Project Objective

The objective of Moodify AI is to combine Artificial Intelligence, Computer Vision and Music Recommendation to create a personalised music discovery experience.

Instead of manually selecting music, users can discover songs based on their detected facial emotions.

## Future Improvements

- Integrate the Spotify Web API for more accurate track information.
- Add direct music playback functionality.
- Improve emotion recognition accuracy.
- Introduce user profiles and personalised listening history.
- Support additional languages and music platforms.
- Develop a mobile-friendly application.



**Moodify AI – Let AI understand your mood and find your music.**
