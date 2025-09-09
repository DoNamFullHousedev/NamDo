import threading
import pyttsx3

def speak(text):
    def _run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=_run, daemon=True).start()