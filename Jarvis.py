
import datetime
import json
import os
import smtplib
import webbrowser

#import autopy
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

path = "c://Users//" + os.getlogin() + "//Desktop//ScreenShots//" + str(datetime.date.today())
try:
    os.makedirs(path)
except FileExistsError:
    pass


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("I Am VECTOR")
    speak("how may i help you sir")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . . ")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        #speak("say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('alok73327@gmail.com', 'balvirji')
    server.sendmail('alokk73327@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak(f"Searching for:{query}\n")    
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'who are you' in query:
            speak("I am Jarvis")
            speak("your personal assistant,sir. i can act on your order.")

        elif 'who am i' in query:
            speak("You are Alok Dubey,sir")

        elif 'hey VECTOR' in query:
            speak("I am here sir")

        elif 'whatsapp' in query:
            speak("Openinng whatsapp")
            webbrowser.open("web.whatsapp.com")

        elif 'facebook' in query:
            speak("Openinng facebook")
            webbrowser.open("facebook.com")
        
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'music' in query:
            speak("here your favorite songs.")
            print("playing music")
            webbrowser.open("https://www.youtube.com/results?search_query=music")

       # elif 'music' in query:
        #    music_dir = 'E:\\Music'
         #   songs = os.listdir(music_dir)
          #  print(songs)
           # os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR,The time is {strTime}")
            print(f"SIR,The time is {strTime}")


        elif 'email' in query:
            try:
                speak("What should I say SIR")
                content = takecommand()
                to = "alok73327@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
                print("Email has been sent")
            except Exception as e:
                print(e)
                print("Sorry Sir, i am not able to send this email at a moment")
                speak("Sorry Sir, i am not able to send this email at a moment")

        elif 'exit' in query:
            exit()

        elif 'news' in query:
            speak("News for today")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3f52edc3c9a945e58348656f101fa866"
            news = requests.get(url).text
            news_json = json.loads(news)
            print(news_json["articles"])
            arts = news_json['articles']
            for articles in arts:
                speak(articles['title'])
                speak("Moving to the next news...listen carefully")

            speak("Thanks for listening...")
