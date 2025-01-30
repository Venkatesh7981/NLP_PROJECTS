document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("speech-to-text-btn").addEventListener("click", async () => {
        const speechOutput = document.getElementById("speech-output");
        speechOutput.value = "Listening...";

        try {
            const response = await fetch("/speech_to_text", { method: "POST" });

            if (!response.ok) {
                throw new Error(await response.text());
            }

            const data = await response.json();
            speechOutput.value = data.text || `Error: ${data.error}`;
        } catch (err) {
            speechOutput.value = `Error: ${err.message}`;
        }
    });

    document.getElementById("text-to-speech-btn").addEventListener("click", async () => {
        const textInput = document.getElementById("text-to-speech-input").value.trim();
        if (!textInput) {
            alert("Please enter text to convert to speech!");
            return;
        }

        try {
            const response = await fetch("/text_to_speech", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: textInput }),
            });

            if (!response.ok) {
                throw new Error(await response.text());
            }

            const data = await response.json();
            alert(data.message || `Error: ${data.error}`);
        } catch (err) {
            alert(`Error: ${err.message}`);
        }
    });
});
