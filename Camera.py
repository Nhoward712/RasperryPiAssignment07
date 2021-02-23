from picamera import PiCamera
from time import gmtime, strftime, sleep
from datetime import datetime
from gpiozero import Button

button = Button(26)
camera = PiCamera()


camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        sleep(2)
        now = datetime.now()
        camera.annotate_text = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        camera.capture('/home/pi/Desktop/Animation/frame'+strftime("%a, %d %b %Y %H:%M:%S", gmtime())+'.jpg' )
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
