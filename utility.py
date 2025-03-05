import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"Index {index}: {voice.name} - {voice.id}")

# List all available microphones
mic_list = sr.Microphone.list_microphone_names()

# Print the list with indexed formatting
print("Available Microphones:\n")
for index, mic_name in enumerate(mic_list):
    print(f"[{index}] {mic_name}")