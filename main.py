import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Smarty"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Smarti A I")
    while True:
        print("Listening....")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}....")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath = r"D:\projects\AI projects\SmartyAI\Assets\tvari-hawaii-vacation-159069.mp3"
            os.startfile(musicPath)

        if "the time" in query:
            musicPath = r"D:\projects\AI projects\SmartyAI\Assets\tvari-hawaii-vacation-159069.mp3"
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        # say(query)
