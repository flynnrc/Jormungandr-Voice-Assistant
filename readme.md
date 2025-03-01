# Voice Assistant with Online/Offline Recognition

This Python script uses the `speech_recognition` library to create a voice assistant that can recognize speech either online or offline, depending on the device's internet connection.

## Features

- **Speech Recognition**: Converts speech to text using either Google Web Speech API (online) or CMU Sphinx (offline).
- **Automatic Mode Switching**: Automatically switches between online and offline modes based on the internet connection.

## Prerequisites

- Python 3.x
- `speech_recognition` library
- `PyAudio` (for microphone input)
- Active internet connection (for Google Web Speech API)

### Installing Dependencies

To install the required dependencies, run the following command:

```bash
pip install SpeechRecognition pyaudio pyttsx3
