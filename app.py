from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
from speech_recognition import Recognizer, Microphone, WaitTimeoutError, UnknownValueError, RequestError


app = Flask(__name__)

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
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            print("Processing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            return "Listening timed out. Please try again."
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Error with the recognition service: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_to_speech', methods=['POST'])
def convert_text_to_speech():
    text = request.json['text']
    text_to_speech(text)
    return jsonify({'message': 'Speech played successfully'})
# app = Flask(__name__)

@app.route('/speech_to_text', methods=['POST'])
def convert_speech_to_text():
    text = speech_to_text()
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
