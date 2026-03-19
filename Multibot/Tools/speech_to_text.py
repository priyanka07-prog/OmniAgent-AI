import speech_recognition as sr

def voice_input():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        return text
    
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    
    except sr.RequestError:
        return "API unavailable"