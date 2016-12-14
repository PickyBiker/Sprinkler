from __future__ import print_function
import module
import os
import sys
import time
import datetime

relays = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7}
pumpPin = 27 # Board pin 13
zonedict = {1:22, 2:13, 3:19, 4:26, 5:12, 6:16, 7:20} # {zone:pin}
BCMpins = [27,22,13,19,26,12,16,20] # BCM pin numbers, pump pin - zone 7

#modefile = {"mode": "off", "zone": "", "pump": "Off", "starttime": [], "stoptime":[]}
#schedulefile = {"zones": "", "waterdays": [], "starttime": [], "stoptime":[]}
    
def main(self):
	# get access to the Sprink class functions
	t = module
	c = module.cl
	
	# shut off all sprinklers
	for pin in relays:
		relays[pin] = 0
	
	# initial mode and schedule file reads
	modefile = c.readmodefile()
	schedulefile = c.readschedulefile()

	lastupdated = os.path.getmtime("mode.json")

	while True:
		currentupdatetime = os.path.getmtime("mode.json")
		lastupdated = 0
		if currentupdatetime != lastupdated:
			c.readmodefile()

			if c.mode == "auto":
# ****************** auto mode **************************
				print("auto mode")
				c.readschedulefile()				
				if c.inrange(c.dstarttime[0], c.dstarttime[1], c.dstoptime[0], c.dstoptime[1]):
					c.sprinkle()
				else:
					c.nosprinkle()

			elif c.mode == "manual":
# ****************** manual mode **************************
				print("manual mode")

			elif c.mode == "off":
# ****************** off mode **************************
				c.nosprinkle
				print("off mode")				
			else:
				print("Invalid 'mode' value in mode.json file")
		else:
			print("file not updated")
			time.sleep(1)
		time.sleep(1)


if __name__=="__main__":
	main(1)