import speech_recognition as sr
import socket
import random
from vpapkg import voice_to_text, print_say

# Function to check if there's an internet connection
def is_online() -> bool:
    try:
        # Try to resolve a common host
        socket.gethostbyname("www.google.com")
        return True
    except socket.error:
        return False

# Initialize recognizer
recognizer = sr.Recognizer()

# Varied greetings
greetings = [
    "Greetings from the depths of Midgard, mortal.",
    "The earth trembles with my presence; I welcome you.",
    "I am the serpent that encircles the world—your arrival has been foretold.",
    "From the shadows beneath the seas, I speak my hello.",
    "The coils of fate twist as I greet you, traveler.",
    "The winds whisper my name as I emerge from the oceans.",
    "With the weight of centuries upon me, I welcome you to my domain.",
    "The world quakes at my words—hello, wanderer.",
    "In the silence of Midgard’s depths, I greet you, bold one.",
    "The serpent stirs; your presence is acknowledged."
]

# Select a random greeting
random_greeting = random.choice(greetings)

# Print the random greeting
print_say(random_greeting)

#TODO merge below into package
while True:
    print('Python is listening...')
    inp = "" 
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            if is_online():
                inp = recognizer.recognize_google(audio)
            else:
                inp = recognizer.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
            pass
        except sr.RequestError as e:
            print("Google error; {0}".format(e))
            pass        
        except sr.WaitTimeoutError:
            print("Timeout")
            pass
    print(f'You just said {inp}.')
    if inp == "banana":
        print('Goodbye!')
        break