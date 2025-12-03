from flask import Flask, Response, render_template, request
import cv2
import requests

app = Flask(__name__)
cap = cv2.VideoCapture(0)
last_frame = None

def generate_frames():
    global last_frame
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        last_frame = frame
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question', '')

    if last_frame is None:
        return "Camera not ready"

    # Encode frame as JPEG
    ret, buffer = cv2.imencode('.jpg', last_frame)
    image_bytes = buffer.tobytes()

    # Send to laptop API (replace with your laptop IP)
    try:
        response = requests.post(
            "http://<LAPTOP_IP>:5001/ask_model",
            files={"image": ("frame.jpg", image_bytes, "image/jpeg")},
            data={"question": question},
            timeout=30
        )
        return response.text
    except Exception as e:
        return f"Error contacting model server: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
