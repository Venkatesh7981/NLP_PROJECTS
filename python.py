import speech_recognition as sr
import pyttsx3


def text_to_speech(text):
    """
    Converts the given text to speech.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speaking speed
    engine.setProperty('volume', 1.0)  # Adjust volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    """
    Converts speech to text using a microphone input.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            recognizer.adjust_for_ambient_noise(source)  # Reduce noise
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error with the recognition service: {e}")
            return None

# Main program
if __name__ == "__main__":
    print("1. Speech-to-Text")
    print("2. Text-to-Speech")
    choice = input("Choose an option (1 or 2): ")
    
    if choice == "1":
        result = speech_to_text()
        if result:
            print(f"Converted Speech to Text: {result}")
    elif choice == "2":
        text = input("Enter the text you want to convert to speech: ")
        text_to_speech(text)
    else:
        print("Invalid choice. Please select 1 or 2.")
