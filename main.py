# main.py

import speech_recognition as sr           # For capturing voice input
import pyttsx3                            # For voice output
from Actions import execute_command       # Importing the custom command handler

# Initialize voice engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text aloud
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to capture voice input
def listen_command():
    with sr.Microphone() as source:
        print(" Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("There is a problem with your internet.")
            return ""

# Main loop
if __name__ == "__main__":
    speak("Voice assistant started. Awaiting your command.")
    while True:
        cmd = listen_command()
        if cmd in ["exit", "quit", "stop"]:
            speak("Goodbye! Shutting down.")
            break
        elif cmd != "":
            execute_command(cmd, speak)
