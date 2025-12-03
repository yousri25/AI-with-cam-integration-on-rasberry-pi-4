```markdown
# Raspberry Pi → Laptop Vision Pipeline

Stream a Raspberry Pi USB camera to a local webpage. The Pi sends the latest frame + your prompt to a laptop on the same LAN. The laptop runs a vision-capable model (Ollama + e.g. `llava:7b`) and returns a text answer shown on the Pi web UI.

Project:
```

project/
├── raspberry_pi.py
├── laptop_server.py
└── templates/
└── index.html

```

IMPORTANT: create `templates/` and put `index.html` inside it.

Quick steps:
1. Edit `raspberry_pi.py` → set `LAPTOP_SERVER_URL = "http://<LAPTOP_IP>:6000/process"`.
2. Install deps (both devices): `pip3 install flask requests opencv-python`
3. On laptop: install Ollama and pull model: `ollama pull llava:7b` (or another image-capable model).
4. Start laptop server: `python3 laptop_server.py`
5. Start Pi server: `python3 raspberry_pi.py`
6. Open browser: `http://<RASPBERRY_PI_IP>:5000` → live stream + ask box.

Notes: both devices must be on the same LAN. If laptop runs out of RAM, use a smaller model or stronger machine. Lower Pi camera resolution (320×240) to speed transfer.
```
