from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
import threading

app = Flask(__name__, static_folder="static", template_folder="templates")

def speak_text(text):
    engine = pyttsx3.init()  # Reinitialize engine every time
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # Ensure engine stops properly after speaking

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech_to_text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening... Speak now!")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            text = recognizer.recognize_google(audio)
            print(f"Recognized text: {text}")  # Debug output
            return jsonify({"text": text})
        except sr.WaitTimeoutError:
            print("Error: Listening timed out.")
            return jsonify({"error": "Listening timed out."}), 400
        except sr.UnknownValueError:
            print("Error: Could not understand audio.")
            return jsonify({"error": "Could not understand."}), 400
        except sr.RequestError as e:
            print(f"Error: {e}")
            return jsonify({"error": f"Request Error: {e}"}), 500
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return jsonify({"error": f"Unexpected Error: {e}"}), 500

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get("text", "")

    if text:
        threading.Thread(target=speak_text, args=(text,)).start()  # Run in separate thread
        return jsonify({"message": "Speaking now!"})
    else:
        return jsonify({"error": "No text provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
