Timelapse script for raspberry pi and the raspicam

If you want this script to run on boot add the following line to /etc/rc.local  
/usr/bin/python /home/pi/raspberry_pi_timelapse/timelapse.py  
or  
\<absolute path to python\> \<absolute path to timelapse.py\>

Be sure to expand your sd card's file system and enable the camera  
You can do so via the command "sudo raspi-config"
