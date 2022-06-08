import time
import os

while True:
	os.system("vcgencmd measure_temp")
	time.sleep (1)
