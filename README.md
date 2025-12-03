# Raspberry Pi → Laptop Vision Pipeline

This project allows you to stream a Raspberry Pi USB camera to a local web interface and send the latest frame along with a text prompt to a laptop running a vision-capable AI model (like LLaVA or Moondream via Ollama). The laptop analyzes the image and returns a text response, which is displayed in the Raspberry Pi web interface.

---

## Project Structure
```

project/
├── raspberry_pi.py      # Raspberry Pi: streams camera + web UI
├── laptop_server.py     # Laptop: receives frame + prompt, runs AI model
└── templates/
└── index.html       # Web UI (must be inside templates/)

```

**Important:** Create a folder named `templates` next to `raspberry_pi.py` and place `index.html` inside it. Flask will not find the webpage otherwise.

---

## Requirements

### Raspberry Pi
- Python 3
- Flask
- OpenCV (`opencv-python`)
- Requests
- USB camera (accessible at `/dev/video0`)

### Laptop
- Python 3
- Flask
- Requests
- Ollama installed
- Vision-capable model pulled into Ollama (example: `ollama pull llava:7b`)
- Enough RAM to run the selected model

---

## Setup & Run

### 1. Configure Pi
In `raspberry_pi.py` set your laptop’s IP:
```

LAPTOP_SERVER_URL = "http://<LAPTOP_IP>:6000/process"

````

### 2. Install dependencies
On both devices:
```bash
pip3 install flask requests opencv-python
````

### 3. Pull AI model on laptop

```bash
ollama pull llava:7b
```

> If your laptop has limited RAM, use a smaller model.

### 4. Start laptop server

```bash
python3 laptop_server.py
```

### 5. Start Raspberry Pi server

```bash
python3 raspberry_pi.py
```

### 6. Access the web interface

Open your browser:

```
http://<RASPBERRY_PI_IP>:5000
```

* See the live camera stream
* Type a question in the input box
* Press **Ask** → Pi sends frame + prompt to laptop → laptop returns response → response shows under the video

---

## Notes & Tips

* Both devices must be on the **same local network**.
* Lower the camera resolution on the Pi (e.g., 320×240) for faster streaming and lower latency.
* If the laptop API times out or runs out of memory, use a smaller model or a machine with more RAM.
* Make sure `templates/index.html` exists and is correctly formatted.
* Monitor both Pi and laptop terminals for errors or warnings.
* You can expand functionality by adjusting Flask routes, camera resolution, or model prompts.

---

## Summary

This setup creates a fully local **Raspberry Pi → Laptop vision chat pipeline**, where the Pi streams video, captures frames on-demand, and the laptop runs AI inference. No cloud connection is required; everything runs on your local network. Perfect for testing vision-language models, AI-assisted monitoring, or interactive robotics projects.

