import speech_recognition as sr
import random
import time
from vpapkg import voice_to_text, print_say

# Initialize recognizer
recognizer = sr.Recognizer()

# Varied Phreases
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
goodbyes = [
    "The seas reclaim me, but I shall return.",
    "The coils of fate loosen, and I take my leave.",
    "The echoes of my presence shall linger—farewell, mortal.",
    "I withdraw to the depths, but our paths may cross again.",
    "The world-serpent slumbers once more—until next time.",
    "The winds whisper my departure, as they once spoke my arrival.",
    "Fate unravels, and so I vanish into the abyss.",
    "The earth ceases its tremors as I fade into legend.",
    "From shadow I came, to shadow I return—farewell.",
    "The tides pull me away, but the waves remember my name."
]
try_again_phrases = [
    "Fate twists—speak again.",
    "The winds did not carry your words.",
    "Destiny coils—try once more.",
    "A whisper in the storm—speak louder.",
    "Midgard does not tremble—try again.",
    "The currents obscure you—speak again.",
    "Your fate is unwritten—repeat yourself.",
    "The echoes fade—try once more.",
    "The serpent listens, but hears not.",
    "Ripples on water—send another wave.",
    "Your words are lost—speak again.",
    "The world waits—try again.",
    "Silence is not an option—speak.",
    "Your voice falters—steady yourself.",
    "The serpent stirs—again!"
]

# Play the random greeting
print_say(random.choice(greetings))

# Flag to track sleep mode and time for sleep mode
sleep_mode = False
sleep_start_time = None

def sleep_loop(greetings, sleep_mode):
    while sleep_mode:
        inp = voice_to_text()
        if inp and inp.lower() == "activate":
            print_say(random.choice(greetings))
            sleep_mode = False
            sleep_start_time = None
        else:
            if sleep_start_time and (time.time() - sleep_start_time >= 30):
                print_say("Snore snore snore...")  # Sleep message after 2 minutes
                sleep_start_time = time.time()
            elif sleep_start_time and (time.time() - sleep_start_time < 30):
                print("Deep Sleep...Zzzz")
            elif sleep_start_time is None:
                sleep_start_time = time.time()
                
try:
    while True:
        #Sleep Loop
        sleep_loop(greetings, sleep_mode)
        #Awake Loop
        print('Python is listening...')
        #Listen For Input
        inp = voice_to_text()   
        #Skip bad input. Try again.
        if not inp:
            print_say(random.choice(try_again_phrases))
            continue
        #Repeat what was said as input.
        inp_lower = inp.lower()
        print_say(f'You just said {inp}.')
        #Map Words to Actions
        if inp_lower == "banana":
            print_say(random.choice(goodbyes))
            break
        elif inp_lower == "sleep":
            sleep_start_time = time.time()
            print_say("The serpent coils into slumber...")
            sleep_mode = True  # Enter sleep mode
        else:
            #ADD Actions Here  
            print("todo...")  
except KeyboardInterrupt:
    #Play the random goodbye
    print_say(random.choice(goodbyes))