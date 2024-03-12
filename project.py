# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import main
import playsound


# Initialize the recognizer
r = sr.Recognizer()

# Set the VAD threshold
vad_threshold = 500

# Set the pause duration
pause_duration = 2

# Function to convert text to speech
def speaktext(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def run():
    while True:
        # Exception handling to handle exceptions at the runtime
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Use VAD to wait for the user to finish speaking
                audio2 = r.listen(source2, phrase_time_limit=None, timeout=None)
                print("Processing audio input...")

                while True:
                    try:
                        # Using google to recognize audio
                        MyText = r.recognize_google(audio2)
                        MyText = MyText.lower()

                        print(MyText)
                        Bool = True
                        main.EVAAI(Bool, MyText)

                        # Exit the loop after a pause_duration
                        r.listen(source2, phrase_time_limit=None, timeout=pause_duration)

                        break

                    except sr.UnknownValueError:
                        # Speech was unintelligible, wait for more speech
                        audio2 = r.listen(source2, phrase_time_limit=None, timeout=None)
                    except sr.WaitTimeoutError:
                        # Speech was too low, prompt user to speak again
                        text = "Sorry, I could not understand you. Please speak clearly into the microphone."

                        language = 'en'

                        speech = gTTS(text=text, lang=language, slow=False)

                        speech.save("text.mp3")
                        # wait for the sound to finish playing?
                        blocking = False

                        playsound.playsound("text.mp3", block=blocking)

                        main.typingPrint("Sorry, I could not understand you. Please speak clearly into the microphone.")

                        audio2 = r.listen(source2, phrase_time_limit=None, timeout=None)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

