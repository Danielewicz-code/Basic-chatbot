import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer() #speech recognition
engine = pyttsx3.init() #text to speech engine


#voice of the chatbot
def voice():
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")


#chatbots listening system
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1) #ignores the ambient noise
            voice = listener.listen(source) #keeps what it listened in the variable voice
            rec = listener.recognize_google(voice, language="en-US") #convert the audio in (voice) into text using googles API
            return rec #we return rec

    #except block if theres any problem with internet connection    
    except sr.RequestError:
        talk("please check your internet connection.")
    return ""


#talk
def talk(text):
    engine.say(text)
    engine.runAndWait()


#interactions
def run():
    voice()
    while True:
        rec = listen()

        if 'hello' in rec:
            talk("hello")

        else:
            talk("Try again")


run()            