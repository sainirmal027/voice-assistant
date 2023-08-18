import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the internet.")
        return ""

def speak(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")

if __name__ == "__main__":
    speak("Hello! I'm your Python voice assistant.")
    while True:
        command = listen().lower()
        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "goodbye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that.")
