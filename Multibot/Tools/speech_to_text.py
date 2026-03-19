import speech_recognition as sr

def voice_input():
    
    with sr.Microphone() as source:
        audio = sr.listen(source)
        
        text = sr.recognize_google(audio)
        
        return text
    