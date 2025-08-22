import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import requests
import os

# Initialize speech and voice
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # speed of voice

# 🔊 Speak function
def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# 🕗 Time and date
def tell_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(f"Current time is {time}")

def tell_date():
    date = datetime.datetime.now().strftime('%B %d, %Y')
    speak(f"Today's date is {date}")

# 🌦️ Weather using OpenWeatherMap API (replace with your key)
def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{base_url}appid={api_key}&q={city}&units=metric"
    response = requests.get(url).json()
    
    if response["cod"] != "404":
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp}°C with {desc}")
    else:
        speak("City not found.")

# ✍️ Notes
def make_note():
    speak("What should I write in your note?")
    with sr.Microphone() as source:
        note_audio = recognizer.listen(source)
        note = recognizer.recognize_google(note_audio)
        with open("jarvis_notes.txt", "a") as f:
            f.write(note + "\n")
        speak("Note saved.")

# 🎵 Play song on YouTube
def play_song_on_youtube():
    speak("Which song do you want to play?")
    with sr.Microphone() as source:
        song_audio = recognizer.listen(source)
        song = recognizer.recognize_google(song_audio)
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

# 📩 WhatsApp message
def send_whatsapp_message():
    speak("Please tell the phone number with country code")
    with sr.Microphone() as source:
        phone_audio = recognizer.listen(source)
        number = recognizer.recognize_google(phone_audio)

    speak("What message should I send?")
    with sr.Microphone() as source:
        msg_audio = recognizer.listen(source)
        message = recognizer.recognize_google(msg_audio)

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2

    pywhatkit.sendwhatmsg(number, message, hour, minute)
    speak("Message scheduled successfully.")

# 📢 Main logic
def process_command(command):
    command = command.lower()

    if "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "joke" in command:
        speak(pyjokes.get_joke())
    elif "note" in command or "write" in command:
        make_note()
    elif "weather" in command:
        speak("Which city's weather do you want?")
        with sr.Microphone() as source:
            city_audio = recognizer.listen(source)
            city = recognizer.recognize_google(city_audio)
            get_weather(city)
    elif "play song" in command:
        play_song_on_youtube()
    elif "send message" in command:
        send_whatsapp_message()
    elif "stop" in command or "exit" in command:
        speak("Goodbye sir!")
        exit()
    else:
        speak("Sorry, I didn't get that.")

# 🎤 Listening loop
if __name__ == "__main__":
    speak("Jarvis initialized. How can I help you?")

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            process_command(command)
        except sr.UnknownValueError:
            speak("Sorry, I didn’t understand. Please repeat.")
        except sr.RequestError:
            speak("Sorry, I’m unable to reach the speech service.")
