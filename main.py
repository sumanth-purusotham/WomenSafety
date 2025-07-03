import os
import queue
import sounddevice as sd
import vosk
import json
import pyttsx3  # Text-to-speech (offline)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Load Vosk model from correct folder path
model = vosk.Model("model")  # Ensure 'model/' contains folders like am/, conf/, etc.

# Queue to store mic audio
q = queue.Queue()

# Microphone input callback
def callback(indata, frames, time, status):
    if status:
        print("⚠️ Mic status:", status)
    q.put(bytes(indata))

# Set up the input audio stream
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("🎤 Listening for voice commands...")

    rec = vosk.KaldiRecognizer(model, 16000)

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            print("Heard:", text)

            # Emergency voice trigger
            if "help me" in text.lower():
                print("🚨 Emergency Triggered!")
                engine.say("Emergency! Help alert activated!")
                engine.runAndWait()

                # Save emergency status to file (optional)
                with open("emergency.txt", "w") as f:
                    f.write("Emergency triggered by voice command.\n")
