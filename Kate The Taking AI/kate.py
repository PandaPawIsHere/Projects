import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) 
engine.setProperty('voice' , voices[1].id)


def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishMe() :
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else :
        speak("Good Evening")

    speak("Hello Sir. I Am Kate, How May I Help You ?")

def takeCommand() :

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable To Recognize, Say That Again Please")
        return "None"
    return query
    
if __name__ == "__main__" :
        wishMe()
        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                 speak("Reaching Wikipedia In Minutes, Please Wait")
                 query = query.replace('wikipedia', "") 
                 results = wikipedia.summary(query, sentences=2)
                 speak("According to Wikipedia")
                 print(results)
                 speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open adobe' in query:
                webbrowser.open("adobe.com")
            
            elif 'play music' in query:
                music_dir = 'E:\\Videos\\MV' 
                songs = os.listdir(music_dir)
                print(songs)
                speak("Playing Songs Form The First One")
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time' in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                print(time)
                speak(f"Sir, The Time Now Is {time}")

            elif 'about you' in query:
                speak("My Name Is Kate The AI Talker. I am made on 9 Of November On The Year 20 22 In India")

            elif 'open visual studio code' in query:
                speak("Opening Visual Studio Code For You, Please Wait")
                loc = "E:\\Softwares\\Library\\Microsoft VS Code\\Code.exe"
                os.startfile(loc)

            elif 'open software directory' in query:
                speak("Opening Software Folder")
                loc = "E:\\Softwares\\Library"
                os.startfile(loc)

            elif 'open games directory' in query:
                speak("Opening Games Folder")
                loc = "E:\\External Games\\Library"
                os.startfile(loc)
            
            elif 'open main directory' in query:
                speak("Opening Main Folder")
                loc = "E:\\Remastered"
                os.startfile(loc)
            
            elif 'open fitgirl website' in query:
                speak("Opening Fitgirl's Website")
                webbrowser.open("fitgirl-repacks.site")
            
            elif 'thank you' in query:
                speak("Your Welcome Sir, Helping You Is My Pleasure.")

        
