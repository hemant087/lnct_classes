import speech_recognition as sr
import pyttsx3
import requests

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert it to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return None
        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return None

# Function to interact with Ollama running Llama 2
def process_with_ollama(input_text):
    api_url = "http://localhost:11434/api/chat"  # Default Ollama API endpoint
    payload = {
        "model": "llama2",  # Name of the model loaded in Ollama
        "messages": [{"role": "user", "content": input_text}]
    }
    
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        result = response.json()
        # Extracting the assistant's reply from Ollama response
        return result.get("messages", [{}])[-1].get("content", "I couldn't generate a response.")
    except requests.exceptions.RequestException as e:
        speak("Error connecting to Ollama.")
        print(e)
        return "Sorry, I encountered an issue."

# Main function to run the assistant
def voice_assistant():
    while True:
        speak("How can I assist you?")
        user_input = recognize_speech()
        if user_input:
            print(f"User said: {user_input}")
            if user_input.lower() in ["exit", "quit", "stop"]:
                speak("Goodbye!")
                break
            
            # Process input with Llama 2 via Ollama
            response = process_with_ollama(user_input)
            print(f"Ollama (Llama 2) response: {response}")
            speak(response)

# Run the voice assistant
if __name__ == "__main__":
    voice_assistant()
