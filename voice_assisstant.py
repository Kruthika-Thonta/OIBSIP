import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
reco=sr.Recognizer()
engine.setProperty("rate", 150)  
engine.setProperty("volume", 1.0)  


def command():
    with sr.Microphone() as source:
        print("Wait for few seconds...\n")
        reco.adjust_for_ambient_noise(source,duration=1)
        print("I'm listening. Please speak now.\n")
        engine.say("I'm listening. Please speak now.")
        engine.runAndWait()
        try:
            audio = reco.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("You didn't start speaking in time.")
            engine.say("You didn't say anything.")
            engine.runAndWait()
            return


    try:
        com=reco.recognize_google(audio,language="en-US")
        print("The message :",format(com))
    except Exception as ex:
        print("Didn't recognised any speech..\n")
        print(ex)
        return

    if "time" in com:
        print(com)
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    elif "hello" in com:
        result="Hello,how can i help you.."
        print(result)
        engine.say(result)
        engine.runAndWait()
    elif "search" in com:
        engine.say("Searching Wikipedia")
        print("Searching Wikipedia...")
        try:
            result = wikipedia.summary(com, sentences=2)
            print(result)
            engine.say(result)
        except Exception as e:
            print("Could not find relevant info.")
            engine.say("Sorry, I couldn't find relevant information.")
        engine.runAndWait()

command()
