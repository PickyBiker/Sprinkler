import json
import datetime

class Sprink(object):
	def __init__(self):
		self.modefile = "" 

	def readmodefile(self):
		try:		
			with open("mode.json") as m:
				self.modefile = json.load(m)
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
		self.mode = self.modefile["mode"]
		self.zone = self.modefile["zone"]
		self.pump = self.modefile["pump"]
		self.mstarttime = self.modefile["starttime"]
		self.mstoptime = self.modefile["starttime"]

	def readschedulefile(self):
		try:		
			with open("schedule.json") as s:
				self.schedulefile = json.load(s)
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
		
			# setup the schedule file data
		self.zones = self.schedulefile["zones"]
		self.waterdays = self.schedulefile["waterdays"]
		self.dstarttime = self.schedulefile["starttime"]
		self.dstoptime =  self.schedulefile["stoptime"]


	# determine if the curren time in within a given time range (24 hour clock)
	def inrange(self, starthour, startmin, stophour, stopmin):
		# Set the now time to an integer that is hours * 60 + minutes
		no = datetime.datetime.now()
		now = no.hour * 60 + no.minute 
		# Set the start time to an integer that is hours * 60 + minutes
		star = datetime.time(starthour, startmin)
		start = star.hour * 60 + star.minute 
	
		# Set the stop time to an integer that is hours * 60 + minutes
		sto = datetime.time(stophour, stopmin)
		stop = sto.hour * 60 + sto.minute

		# handle midnight by adding 24 hours to stop time and now time
		if stop < start:
			stop += 1440
			now += 1440 
		#see if we are in the range
		if start <= now < stop:
			return True
		return False

	def sprinkle(args):
		# turn the sprinkler on
		print("sprinkling")

	def nosprinkle(args):
		# turn the sprinkler off
		print("not sprinkling")

cl = Sprink()