// Handle Speech-to-Text
document.getElementById("speech-to-text-btn").addEventListener("click", async () => {
    const speechOutput = document.getElementById("speech-output");
    const speechToTextBtn = document.getElementById("speech-to-text-btn");
  
    // Update UI to show loading state
    speechToTextBtn.textContent = "Listening...";
    speechToTextBtn.disabled = true;
    speechOutput.value = "Processing your speech...";
  
    try {
      const response = await fetch("/speech_to_text", { method: "POST" });
  
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Server Error: ${errorText}`);
      }
  
      const data = await response.json();
      if (data.text) {
        speechOutput.value = data.text;
      } else {
        throw new Error(data.error || "Unknown error from server");
      }
    } catch (err) {
      speechOutput.value = `Error: ${err.message}`;
    } finally {
      // Reset button state
      speechToTextBtn.textContent = "Start Listening";
      speechToTextBtn.disabled = false;
    }
  });
  
  // Handle Text-to-Speech
  document.getElementById("text-to-speech-btn").addEventListener("click", async () => {
    const textInput = document.getElementById("text-to-speech-input").value;
    const textToSpeechBtn = document.getElementById("text-to-speech-btn");
  
    if (!textInput.trim()) {
      alert("Please enter text to convert to speech!");
      return;
    }
  
    // Update button state
    textToSpeechBtn.textContent = "Speaking...";
    textToSpeechBtn.disabled = true;
  
    try {
      const response = await fetch("/text_to_speech", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: textInput }),
      });
  
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Server Error: ${errorText}`);
      }
  
      const data = await response.json();
      if (data.message) {
        alert(data.message);
      } else {
        throw new Error(data.error || "Unknown error from server");
      }
    } catch (err) {
      alert(`Error: ${err.message}`);
    } finally {
      // Reset button state
      textToSpeechBtn.textContent = "Speak";
      textToSpeechBtn.disabled = false;
    }
  });
  