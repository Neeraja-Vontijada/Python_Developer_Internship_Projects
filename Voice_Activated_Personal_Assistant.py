import speech_recognition as sr
import pyttsx3
import requests
import pyaudio
# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level

# Function to speak out a text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        # Convert audio to text
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        speak("Error with the speech service.")
        return None

# Simulated weather data
weather_data = {
    "London": {"description": "clear sky", "temperature": 15},
    "Paris": {"description": "partly cloudy", "temperature": 18},
    "New York": {"description": "light rain", "temperature": 12},
    "Tokyo": {"description": "sunny", "temperature": 22},
}

# Function to get simulated weather
def get_weather(city):
    city = city.capitalize()
    if city in weather_data:
        weather = weather_data[city]["description"]
        temperature = weather_data[city]["temperature"]
        return f"The weather in {city} is {weather} with a temperature of {temperature} degrees Celsius."
    else:
        return "Sorry, I don't have weather data for that city."

# Main function
if __name__ == "__main__":
    speak("Hello! How can I assist you?")
    
    while True:
        user_input = get_voice_input()
        
        if user_input:
            user_input = user_input.lower()
            
            # Check weather
            if "weather" in user_input:
                speak("Which city would you like to check?")
                city = get_voice_input()
                if city:
                    weather_info = get_weather(city)
                    speak(weather_info)
            
            # Exit the assistant
            elif "exit" in user_input or "quit" in user_input or "stop" in user_input:
                speak("Goodbye!")
                break
            
            else:
                speak("Sorry, I didn't get that. You can ask about the weather, or say 'exit' to quit.")
