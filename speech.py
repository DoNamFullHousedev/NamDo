import speech_recognition as sr

def recognize_speech(language="en-US"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""