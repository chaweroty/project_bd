import speech_recognition as sr
from gtts import gTTS
import playsound
import os

class Assistant:
    @staticmethod
    def speak(message):
        tts = gTTS(text=message, lang="es", slow=False)
        filename = os.path.join(os.path.dirname(__file__), "voice.mp3")
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    @staticmethod
    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening ...")
            Assistant.beep()
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio, language='es-ES')
            except Exception as e:
                print("Exception: " + str(e))

        return said

    @staticmethod
    def beep():
        filename = os.path.join(os.path.dirname(__file__), "sounds", "beep.mp3")
        playsound.playsound(filename)
