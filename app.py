import streamlit as st
import speech_recognition as sr
import pyttsx3
import json

# Text to Speech function
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# Speech to Text function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now!")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            return "Listening timed out."
        except sr.UnknownValueError:
            return "Sorry, could not understand."
        except sr.RequestError as e:
            return f"Error: {e}"

# Frontend HTML with buttons and inputs (using Streamlit components)
st.markdown("""
    <html>
    <head>
        <script type="text/javascript" src="static/script.js"></script>
        <link rel="stylesheet" href="static/styles.css">
    </head>
    <body>
        <h1>Speech to Text & Text to Speech</h1>
        
        <!-- Text-to-Speech Section -->
        <div>
            <input id="text-to-speech-input" type="text" placeholder="Enter text to convert to speech">
            <button id="text-to-speech-btn">Speak</button>
        </div>

        <!-- Speech-to-Text Section -->
        <div>
            <button id="speech-to-text-btn">Start Listening</button>
            <textarea id="speech-output" placeholder="Speech output will appear here"></textarea>
        </div>
    </body>
    </html>
""", unsafe_allow_html=True)

# Define routes (you'll use Streamlit buttons instead of actual routing)
if st.button("Start Speech Recognition"):
    speech_text = speech_to_text()
    st.text(speech_text)

if st.button("Convert Text to Speech"):
    user_input = st.text_input("Enter Text for Speech Conversion:")
    if user_input:
        text_to_speech(user_input)
        st.success("Text to speech conversion completed!")
