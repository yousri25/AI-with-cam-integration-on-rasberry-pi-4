Raspberry Pi Remote AI Camera Assistant

This project lets you stream your Raspberry Pi USB camera to a local webpage and ask questions about the live image using a vision-enabled AI model (such as LLaVA) running on your laptop or PC.

The Raspberry Pi handles:

Live camera feed

Sending the latest frame + your question to your laptop

Your laptop handles:

Running Ollama

Running a vision model (recommended: llava:7b)

Processing frames and returning responses

Features

Live camera streaming from Raspberry Pi

Simple web interface

Ask questions about what the camera sees

Laptop performs the AI inference

Works over local network (LAN)

Project Structure
project/
│── pi_app.py
│── laptop_api.py
│── templates/
│     └── index.html

IMPORTANT WARNING

You MUST create a folder named templates in the same directory as pi_app.py and put index.html inside it.

If the templates folder does not exist, Flask will not find the webpage.

Raspberry Pi Setup

Install dependencies:

sudo apt update
sudo apt install python3-flask python3-opencv fswebcam


Run the Raspberry Pi backend:

python3 pi_app.py

Laptop / PC Setup

Install Ollama (from https://ollama.com/download

)

Pull a vision model:

ollama pull llava:7b


Run the laptop API:

python3 laptop_api.py

Accessing the Web Interface

Open a browser and go to:

http://<RPI_IP_ADDRESS>:5000


You will see:

Live camera stream

A text box to ask questions

AI answers based on the camera feed
