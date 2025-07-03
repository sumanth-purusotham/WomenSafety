# Women's Safety App (Voice-Activated Emergency Tool)

### ⚠️ Project Status: On Hold / Incomplete  
> *"I failed to build a great idea, but in the future, if I collect more knowledge, I will restart this project." – Sumanth*

---

## 🔍 Overview

This app was designed with the goal of helping women in emergency situations using **offline voice commands**. The core idea was to create a **touchless emergency alert system** using voice recognition and automated calling/SMS features.

### 🧠 Project Concept
- Voice commands like “help me” or “danger” trigger emergency action
- Automatically calls or texts a saved emergency contact
- Works fully **offline**
- Built using:
  - [Kivy](https://kivy.org/) for UI and app logic
  - [Vosk](https://alphacephei.com/vosk/) for offline voice recognition
  - [Plyer](https://plyer.readthedocs.io/en/latest/) for phone features like calling/SMS
  - [Buildozer](https://github.com/kivy/buildozer) to compile for Android

---

## 🛠️ Tech Stack

| Component         | Tool/Library |
|------------------|--------------|
| UI & Logic       | Kivy         |
| Voice Recognition| Vosk         |
| Device Access    | Plyer        |
| Android Packaging| Buildozer    |
| Platform         | WSL2 (Ubuntu), Python VirtualEnv |

---

## 🔧 Current Problems
- Buildozer failed while compiling the APK for Android
- Multiple dependency and compatibility issues inside WSL
- Some native Android permissions not working properly
- `sounddevice` and `vosk` integration failed inside the APK build

---

## 📁 Folder Structure (When I paused)
