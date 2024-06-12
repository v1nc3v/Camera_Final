# Vincent Ton
# June 11, 2024
# This script sets up the live web stream with Flask

from flask import Flask, render_template, Response, request
import cv2
import time
import os

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html', res_str=result)
                        
    return render_template('index.html')

app.route('/video')
def video():
    return Response(generate(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate(camera):
    while True:
        # read the camera frame
        success, frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg', frame)
            frame=buffer.tobytes()
        
    yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
       
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

# background process
@app.route('/left')
def left():
    print ("Left")
    os.system("python servo.py 1 2 0.1 1 1 1")       
    return ("nothing")
    
@app.route('/up')
def up():
    print ("Up")
    os.system("python servo.py 1 2 0.1 1 1 2")       
    return ("nothing")

@app.route('/center')
def center():
    print ("Center")
    os.system("python servo.py 89 90 0.3 1 1")       
    return ("nothing")

@app.route('/down')
def down():
    print ("Down")
    os.system("python servo.py 1 2 0.1 1 1 2")       
    return ("nothing")

@app.route('/right')
def right():
    print ("Right")
    os.system("python servo.py 179 180 0.1 1 1")       
    return ("nothing")
