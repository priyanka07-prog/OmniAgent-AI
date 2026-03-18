import speech_recognition as sr

def voice_input():
    
    with sr.Microphone() as source:
        audio = r.listen(source)
        
        text = r.recognize_google(audio)
        
        return text