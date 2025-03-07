# Get rid of ALSA lib error messages in Linux
import platform
from .connectivity import is_online

if  platform.system() == "Linux":
    from ctypes import *
    
    # Define error handler
    error_handler = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
    # Don't do anything if there is an error message
    def py_error_handler(filename, line, function, err, fmt):
      pass
    # Pass to C
    c_error_handler = error_handler(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
	
# Now define the voice_to_text() function for all platforms    
import speech_recognition as sr

recognizer = sr.Recognizer()
def voice_to_text():
    voice_input = "" 
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            if is_online():
                voice_input = recognizer.recognize_google(audio)
            else:
                voice_input = recognizer.recognize_sphinx(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass        
        except sr.WaitTimeoutError:
            pass
    return voice_input