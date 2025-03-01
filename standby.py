import speech_recognition as sr
import socket

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