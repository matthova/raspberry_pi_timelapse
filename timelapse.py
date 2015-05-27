import time
import picamera
import os
time_between_photos = 60 * 60 # one photo per hour

directory = os.getcwd() + "/photos/"
if not os.path.exists(directory):
    os.makedirs(directory)

camera = picamera.PiCamera()

while True:
	filename = directory + "image " + str(int(time.time())) + ".jpg"
	camera.capture(filename)
	time.sleep(time_between_photos)
