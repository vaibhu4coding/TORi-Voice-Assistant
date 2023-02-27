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
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from TORIGUITEST import Ui_TORiUi
import pywikihow
from pywikihow import search_wikihow
import requests
import smtplib
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Tori honour, how can I help you?")


def speak(audio):
    engine.say(audio)   
    print(audio)  
    engine.runAndWait()   

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        self.execute()
        
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...")
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

    def execute(self):
        wish()
        while True:
            self.query = self.takecommand().lower()
            #logic building for tasks

            if "open command prompt" in self.query:
                os.system("start cmd")
                
            elif "i want information" in self.query:
                speak("Which information do you want?")
                self.query = self.query.replace("i want information", self.takecommand())
                results = wikipedia.summary(self.query, sentences=2)
                speak(f"according to wikipedia {self.query} is ")
                speak(results)
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")
            elif "open instagram" in self.query:
                webbrowser.open("www.instagram.com")
            elif "play song" in self.query:
                speak("Which song you want to play?")
                song_name = self.takecommand()
                kit.playonyt(f"{song_name}")
                sys.exit()
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            elif "open whatsapp" in self.query:
                webbrowser.open("https://web.whatsapp.com/")
                sys.exit()
            elif 'open google' in self.query:
                webbrowser.open('google.com')

            elif "open twitter" in self.query:
                webbrowser.open("https://twitter.com/")
                sys.exit()

            elif "open android" in self.query:
                webbrowser.open("https://android.com/")
                sys.exit()
                
            elif "go to sleep" in self.query:
                speak("Ok sir have a good day")
                sys.exit()

            elif "time now" in self.query:
                global time
                time = "The time is " +  datetime.datetime.now().strftime('%I:%M %p')
                speak(time)

            elif "open mail" in self.query:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif 'open hackerrank' in self.query:
                webbrowser.open('hackerrank.com')
            
            elif 'open stack overflow' in self.query:
                webbrowser.open('stackoverflow.com')

            elif 'stock market' in self.query:
                speak("See the update honour")
                webbrowser.open('https://www.investing.com/')
                sys.exit()
                
            elif 'activate how to do' in self.query:
                speak("Activated!Honour please tell me what you want to know?")
                how = self.takecommand().lower()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

            elif ' open zoom'  in self.query:
                webbrowser.open('https://zoom.us/meetings')
            elif "no thanks" in self.query:
                speak("have a good day honour")
                sys.exit()
            elif "set a reminder" in self.query:
                speak("what is the topic of the reminder")
                topic = self.takecommand().lower()
                speak("at what time do you want it to be reminded to you")
                momory = self.takecommand().lower()
                rescue = "Don't forget about" + topic + "" + "at" + momory
                speak(rescue)
                momory = momory.replace(",","")
                momory = momory.upper()
                import MyAlarm
                MyAlarm.alarm(momory)
            

            elif "temperature" in self.query:
                search = "temperature in india"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div" ,class_="BNeawe").text
                weather = f"Currently in INDIA it is {temp} with hazz"
                speak(weather)
                speak(f"Today it will be partly sunny with a forcast tie of {temp}")

            elif "glad to meet you tori" in self.query:
                speak("thank you honour...giving todays update")
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
                speak("Honour always be a believer")
                kit.playonyt('believer')
                speak("Have a good day honour")
                sys.exit()

            elif "repeat after me" in self.query:
                speak("What would me you like to repeat?")
                rep1 = self.takecommand().lower()
                speak("you said")
                speak(rep1)

            elif "play" in self.query:
                song = self.query.replace('play', '')
                speak('playing ' + song)
                kit.playonyt(song)
                sys.exit()
                
            elif "none" in self.query:
                print("none")

            elif "translate" in self.query:
                webbrowser.open("https://translate.google.co.in/")
                sys.exit()

            elif "date" in self.query:
                date = datetime.datetime.now().strftime('%d %B %Y')
                speak(f"Today's date is {date}")

            elif "what is your name" in self.query:
                speak("Just a rather very interesting system")
                speak(" in short TORI BEZOS you can simply call me Tori")

            elif "how old are you" in self.query:
                speak(" i am very old to use internet but i am very young to sing a song")

            elif "news" in self.query:
                speak("Here is the latest news")
                webbrowser.open("https://news.google.co.in/")
                sys.exit()

            elif "discord" in self.query:
                speak("opening discord")
                webbrowser.open("https://discord.com")


            elif "flip a coin" in self.query:
                speak("fliping a coin")
                webbrowser.open("https://www.google.com/search?q=flip+a+coin")
                sys.exit()
                
            elif "shut down laptop" in self.query:
                os.system("shutdown /s /t 5")
                sys.exit()
            speak("Aur kuch?")
            
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TORiUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("image_processing20200620-21668-36w7bn.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("loader_sci-fi.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("loader_sci-fi.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("loader_sci-fi.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("voice effect 2.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("8871.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_date)
        self.ui.textBrowser_3.setText(label_time)
app = QApplication(sys.argv)
tori = Main()
tori.show()
exit(app.exec_())   
 