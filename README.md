
##            ✋🗿📄 Hand Gesture RPS-Duel (Gesture Edition) 🎮 
![Python](https://img.shields.io/badge/Python-blue) 
![cvzone](https://img.shields.io/badge/cvzone-recognition-green)
![mediapipe](https://img.shields.io/badge/mediapipe-tracking-orange)
![pyttsx3](https://img.shields.io/badge/pyttsx3-textToSpeech-blue)
![opencv](https://img.shields.io/badge/opencv-python-blue)


## ✨Overview
This project is an interactive Rock, Paper, Scissors game where players use hand gestures to make their move. The game employs real-time hand tracking and voice feedback to create a dynamic and engaging experience. The AI opponent makes a random choice, and the game announces the result using text-to-speech.

## ✨ Features

- **Real-Time Hand Gesture Recognition :** Detects hand gestures to determine the player's move (Rock, Paper, or Scissors).
- **Voice Feedback :** Provides audible feedback on game outcomes using text-to-speech technology.
- **AI Opponent:** The computer randomly selects its move, ensuring each game is different.
- **User-Friendly Interface:** Displays the webcam feed and processes gestures in real-time.

## ✨Technologies Used
- **Hand Tracking :** `cvzone` library for detecting and interpreting hand gestures.
- **Voice Feedback:** `pyttsx3` library for generating voice output.
- **Computer Vision:** `OpenCV` for capturing video from the webcam.

## ✨Requirements
- **Python 3.x**: The programming language used for development.
- **cvzone**: For hand tracking and gesture recognition.
- **mediapipe**: Required by `cvzone` for hand tracking functionality.
- **pyttsx3**: For text-to-speech capabilities.
- **opencv-python**: For video capture and display.

To install the required packages, run the following command:

```bash
pip install cvzone mediapipe pyttsx3 opencv-python


