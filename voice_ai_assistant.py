
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(audio):
    print(f"Talking: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    talk('I am Vista, your personal assistant created by vishakha')
    wish = (datetime.datetime.now().strftime("%p"))
    if wish == 'AM':
        talk('Good morning')
    else:
        talk('Good evening')


wishMe()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return command

def run_rolex():
    command = take_command().lower()
    print(f"Command received: {command}")  

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song} for you')
        pywhatkit.playonyt(song)

    elif command == 'hai':
        talk('Hello!')

    elif command == 'how are you':
        talk('I am fine. What about you?')

    elif command == 'who are your parents':
        talk('I was created by my team, KG10')

    elif command == 'are you single':
        talk('No, I am committed')

    elif command == 'what is your number':
        talk('My IP address is 192.15.36.285')

    elif command == 'rolex':
        talk('Hi, how can I help you?')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%x')
        talk('Current date is ' + date)

    elif 'youtube' in command:
        webbrowser.open("https://www.youtube.com/")

    elif 'open google' in command:
        subprocess.call(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    elif 'open spotify' in command:
        webbrowser.open("https://open.spotify.com/") 

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'my music' in command:
        talk('Playing music')
        webbrowser.open("https://www.youtube.com/watch?v=hCt-H4-5wco&list=RDhCt-H4-5wco&start_radio=1")

    elif 'whatsapp' in command:
        talk('Opening WhatsApp')
        webbrowser.open("https://web.whatsapp.com/")

    elif 'mail' in command:
        talk('Opening Gmail')
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif 'maps' in command:
        talk('Opening Google Maps')
        webbrowser.open("https://www.google.com/maps")

    elif 'neocolab' in command:
        talk('Opening NeoColab')
        webbrowser.open("https://neocolab.srmap.edu.in/")

    elif 'movies' in command:
        talk('Opening movies')
        webbrowser.open("https://ww4.ibomma.cc/telugu-movies/")

    elif 'linkedin' in command:
        talk('Opening LinkedIn')
        webbrowser.open("https://in.linkedin.com/")

    elif 'netflix' in command:
        talk('Opening Netflix')
        webbrowser.open("https://www.netflix.com/in/")

    elif 'prime' in command:
        talk('Opening Amazon Prime')
        webbrowser.open("https://www.primevideo.com/in")

    elif 'gopal' == command:
        talk('Opening GK in Browser')
        webbrowser.open("https://gopalakrishnaparimi.blogspot.com/")

    elif "wait" == command:
        talk("I will wait for you.")
        time.sleep(5)  


    elif 'news' in command:
        talk('Here is the latest news update:')
        webbrowser.open("https://www.bbc.com/news")

    elif 'podcast' in command:
        talk('Here is a random podcast for you.')
        webbrowser.open("https://www.listennotes.com/c/24f4ad5c3b2f48a2bc59f206a0a8b8fe/")

    elif 'radio' in command:
        talk('Starting the radio show now.')
        webbrowser.open("https://www.youtube.com/watch?v=hCt-H4-5wco&list=RDhCt-H4-5wco&start_radio=1")

    else:
        talk('Please say the command again.')

if __name__ == "__main__":

    while True:
        run_rolex()
