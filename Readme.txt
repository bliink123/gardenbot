GardenBot

Aim:
Have a monitored garden, that can be watered remotely.

Possible Features:
Check temp and soil moisture
Display weather forecast
Give option to water garden
Chart temp and moisture


RPi will host webserver
Python Script will run on PiServer to update webpage
Python Script will monitor serial port for temp and moisture data from arduino 
Arduino will monitor sensors and write to serial 
Arduino will control relay to toggle servo valve 
