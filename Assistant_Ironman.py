import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

# TẠO ĐỐI TƯỢNG
friday = pyttsx3.init()

# LẤY GIỌNG
voice = friday.getProperty('voices')

# SET GIỌNG (0: Nam, 1: Nữ)
friday.setProperty('voice', voice[1].id)

# HÀM NÓI VÀ IN RA MÀN HÌNH
def speak(audio):
    print("Friday: " + audio)
    friday.say(audio)
    friday.runAndWait()

#HÀM LẤY THỜI GIAN
def time():
    # Lấy thời gian hiện tại(%I giờ 12h, %M phút, %p     AM/PM)
    Time = datetime.datetime.now().strftime("%I: %M: %p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good night sir")
    speak("How can I help you ?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en-US')
        print("Tony Stark: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input('Your order is: '))
        print("Tony Stark: " + query)
    return query
# HÀM CHÍNH
if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search, sir ?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
            
        elif "youtube" in query:
            speak("What should I search, sir ?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
 
        elif "open video" in query:
            meme = r"D:\WORKSPACE\PYTHON\Project_QRCode\video\cat.mp4"
            os.startfile(meme)

        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Friday is off, Goodbye sir")
            quit()