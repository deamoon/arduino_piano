import serial
import requests
import time

# URL = 'http://localhost:5000/piano/get'
URL = "https://powerful-mountain-8361.herokuapp.com/piano/get"

ser = serial.Serial('/dev/ttyACM0', 9600)

# http://goo.gl/ZPjLOZ
notes = [131, 139, 147, 156, 165, 175, 185, 196, 207, 220, 233, 247, # small C-B
		 262, 277, 293, 311, 330, 349, 370, 392, 415, 440, 466, 494, # first C-B
		 523, 554] # second C-C#

def idToNote(id):
	return str(notes[id + 12])

cur_id = -1
while True:
	r = requests.get(URL)
	if r.status_code == 200:
		data = r.json()
		if cur_id == -1:
			cur_id = data[-1][0]
		for d in data:
			if d[0] > cur_id:				
				ser.write(idToNote(d[1]) + '\n')
				cur_id = d[0]
				time.sleep(0.2)
				ser.write('0' + '\n')
				time.sleep(0.5)
	# time.sleep(1)
