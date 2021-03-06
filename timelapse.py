import time
import picamera
import os
time_between_photos = 60 * 60# one photo per hour

directory = os.getcwd() + "/photos/"
if not os.path.exists(os.getcwd() + "/photos"):
	os.makedirs(directory)

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

while True:
	filename = directory + "image " + str(int(time.time())) + ".jpg"
	camera.capture(filename)
	time.sleep(time_between_photos)
