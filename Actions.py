# actions.py

import os
import webbrowser
import pyautogui
import wikipedia

def execute_command(command, speak):
    command = command.lower().strip()

    # 1. OPEN APPLICATIONS
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    elif "open chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("start calc")

    # 2. SEARCH ON GOOGLE
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Please say what to search.")

    # 3. TYPE TEXT
    elif "type" in command:
        text = command.replace("type", "").strip()
        if text:
            pyautogui.write(text)
            speak("Typed the text.")
        else:
            speak("Please say the text to type.")

    # 4. CLOSE APPLICATIONS
    elif "close notepad" in command:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "close chrome" in command:
        speak("Closing Chrome")
        os.system("taskkill /f /im chrome.exe")

    # 5. BASIC OS ACTIONS
    elif "lock my screen" in command:
        speak("Locking the screen")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "shutdown my computer" in command:
        speak("Shutting down the computer")
        os.system("shutdown /s /t 5")

    elif "restart my computer" in command:
        speak("Restarting the computer")
        os.system("shutdown /r /t 5")
    
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "play music on youtube" in command:
        query = command.replace("play music on youtube", "").strip()
        if query:
            speak(f"Playing {query} on YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        else:
            speak("Please say what song to play.")

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia, {result}")
        except:
            speak("Sorry, I couldn't fetch the information.")          
    

    # 6. Fallback
    else:
        speak("Sorry, I don't understand that command yet.")
