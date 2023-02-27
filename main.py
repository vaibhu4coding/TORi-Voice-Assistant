import pyttsx3
import speech_recognition as sr 
import datetime
import os
import cv2
import wikipedia
import webbrowser
import pywhatkit as kit 
import pyjokes
import sys
import pywhatkit
from bs4 import BeautifulSoup
import requests
import pywikihow
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


#it will convert text to speech
def speak(audio):
    engine.say(audio)   
    print(audio)  
    engine.runAndWait()   

#it will convert speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#it will wish good morning, good evening, etc
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am TORi honour, how can I help you?")

#ye function sirf usi .py file m chalega
if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        #logic building for tasks

        if "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "i want information" in query:
            speak("Which information do you want?")
            query = query.replace("i want information", takecommand())
            results = wikipedia.summary(query, sentences=2)
            speak(f"according ot wikipedia {query} is ")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "play song on youtube" in query:
            speak("Which song you want to play?")
            song_name = takecommand()
            kit.playonyt(f"{song_name}")
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
 
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
            sys.exit()    
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif "open twitter" in query:
            webbrowser.open("https://twitter.com/")
            sys.exit()

        elif "open android" in query:
            webbrowser.open("https://android.com/")
            sys.exit()
            
        elif "go to sleep" in query:
            speak("Ok sir have a good day")
            sys.exit()

        elif "time now" in query:
            global time
            time = "The time is " +  datetime.datetime.now().strftime('%I:%M %p')
            speak(time)

        elif "open mail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open hackerrank' in query:
            webbrowser.open('hackerrank.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'stock market' in query:
            webbrowser.open('https://www.investing.com/')

        elif ' open zoom'  in query:
            webbrowser.open('https://zoom.us/meetings')
        elif 'open VS' in query:
            codepath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "set a reminder for tomorrow" in query:
            speak("what is the topic of the reminder")
            topic = takecommand().lower()
            speak("at what time do you want it to be reminded to you")
            momory = takecommand().lower()
            rescue = "Don't forget about" + topic + "" + "at" + momory

        elif "temperature" in query:
            search = "temperature in india"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div" ,class_="BNeawe").text
            weather = f"Currently in INDIA it is {temp} with hazz"
            speak(weather)
            speak(f"Today it will be partly sunny with a forcast tie of {temp}")

        elif "good morning" in query:
            speak("good morning adi")
            time = "The time is " +  datetime.datetime.now().strftime('%I:%M %p')
            speak(time)
            search = "temperature in india"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div" ,class_="BNeawe").text
            weather = f"Currently in INDIA it is {temp} with hazz"
            speak(weather)
            speak(f"Today it will be partly sunny with a forcast tie of {temp}")
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
            speak("playing senorita")
            pywhatkit.playonyt('senorita')
            speak("Have a good day sir")
            sys.exit()


        elif "play" in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            sys.exit()
            
        elif "none" in query:
            print("none")

        elif "translate" in query:
            webbrowser.open("https://translate.google.co.in/")
            sys.exit()

        elif "date" in query:
            date = datetime.datetime.now().strftime('%d %B %Y')
            speak(f"Today's date is {date}")

        elif "what is your name" in query:
            speak("Just a rather very interesting system")
            speak(" in short TORI BEZOS you can simply call me TORi")

        elif "how old are you" in query:
            speak(" i am very old to use internet but i am very young to sing a song")

        elif "what is my name" in query:
            speak("your name is Aditya")

        elif "news" in query:
            speak("Here is the latest news")
            webbrowser.open("https://news.google.co.in/")
            sys.exit()
        
        elif "wake up" in query:
            speak("Good morning Aditya")
            music_dir = "C:\\Users\\xyz\\Desktop\\Google\\iPad Pro — Float.mp4"
            os.startfile(music_dir)
            sys.exit()

        elif "discord" in query:
            speak("opening discord")
            webbrowser.open("https://discord.com")


        elif "flip a coin" in query:
            speak("fliping a coin")
            webbrowser.open("https://www.google.com/search?q=flip+a+coin")
             

        elif "shut down laptop" in query:
            os.system("shutdown /s /t 5")
        elif "restart laptop" in query:
            #3rd video dekh lena playlist ka
            print()
        speak("Aur kuch?") #isko formal msg m convert krna
    #youtube ka playlist dekh lena
    #aur accordingly tuze jo feature ache lage wo add 
    #krlena aur khudke features bhi add krlena
    #all the best... :)
    #ye elif ki jagah kuch aur use hosakta hai kya wo bhi dekh lenaa...
    #upar jo files import kiya hai wo already installed h kya tereme wo dekh lena
    #pip install package Ka Naam dekhne keliye 2nd video dekhna playlist ka