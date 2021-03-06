#!/usr/bin/python
import pdb
import sys
#
# This reads adventure.dat, which is a simple text file.
# This is going to need a __main__ and all those goodies, as
# well as defining the place as dark or not and defining objects better.

# For Section 5
class Item():
	def __init__(self,itemnumber,propertyvalue,inventorymessage):
		self.itemnumber = itemnumber
		self.propertyvalue = propertyvalue
		self.inventorymessage = inventorymessage
		self.moveable = True
		self.initiallocation = 0
		self.secondlocation = 0

	def moveable(self,moveable):
		self.moveable = moveable

	def __getattr__(self,moveable):
		self.moveable	

	def initiallocation(self, initiallocation):
		self.initiallocation = initiallocation

	def secondlocation(self, secondlocation):
		self.secondlocation = secondlocation

	def debug(self,itemnumber,propertyvalue,inventorymessage,moveable,initiallocation,secondlocation):
		print "itemnumber", str(self.itemnumber)
		print "propertyvalue", str(self.propertyvalue)
		if inventorymessage:
			print "inventorymessage",str(self.inventorymessage)
		else:
			print "no inventory message"
		print "Is it moveable? ", 
		print moveable
		print "location 1:", str(self.initiallocation)
		print "location 2:", str(self.secondlocation)

# I think of different locations as rooms. Oh well. They have properties,
# like if they have been visited already, long descriptions and short
# descriptions.
#
class Location:
	def __init__(self,roomname,visited,long_description):
		self.roomname = roomname
		self.visited = visited
		self.long_description = long_description
		self.short_description = "PENDING SHORT_DESCRIPTION - this might not actually be a location."
		self.traveltable = makeemptyarray()

	def short_description(self,short_description):
		self.short_description = short_description

	def redoarray(self, traveltable):
		self.traveltable = traveltable

	def debug(self,roomname,visited,long_description,short_description):
		print "+----------------------------------------------"
		print "ROOMNAME ", self.roomname
		print "VISITED ", self.visited
		print "LONG DESCRIPTION ", self.long_description
		print "SHORT DESCRIPTION " , self.short_description

def makeemptyarray():
	i = 0
	emptyactionarray = []
	while ( i < 300 ):
		emptyactionarray.append("i")
		i += 1
	return emptyactionarray


amsg = makeemptyarray

try : 
	textfiletoread = open('advent.dat','r')
except:
	print "Can't find data file to open."
	sys.exit()

section = 1 # Section 1 in the data file
roomtable = {} #Stores the classes for each room
roomlisttable = {} #Dictionary of rooms of class Location
itemlisttable = {} #Dictionary of items of class Item
inputs = {} #Maps word to a number, ex inputs["ROAD"] = 2
itemtable = {}
amsg = {}

# START READING FILE
for x in textfiletoread.readlines():
	x = x.rstrip('\n') #Replaces Perl chomp
	temp = x.split('	')
	# For now just put long descriptions in a hash
	# Section 1 section 1
	if ( section == 1 ):
		if ( len(temp) > 1 ):
			roomname = "ROOM" + str(temp[0])
			roomlisttable[roomname] = roomname
			if roomname in roomtable:
				if ( roomtable[roomname].long_description ):
					x = roomtable[roomname].long_description
					x = x + " " + temp[1]
					roomtable[roomname].long_description = x
			else:
				roomtable[roomname] = Location(roomname,False,temp[1])
	# section 2 Section 2
	if ( section == 2 ):
		if ( len(temp) > 1 ):
			roomname = "ROOM" + str(temp[0])
			if roomname in roomtable:
				# assign class short_location thing here
				roomtable[roomname].short_description = temp[1]			
			else:
				pass 

	# section 3 Section 3
	# First number is the current room. Second is the next room.
	# The rest are the commands that get you into that next room.
	# Use that to build this class's travel table
	if ( section == 3 ):
		if ( roomname ):
			oldroomname = roomname	
		if ( len(temp) > 2 ):
			roomname = "ROOM" + str(temp[0]) #Definitely the room
			del temp[0]
			# Some of the "nextroom numbers are crazy high.
			# need to wrap logic around that.
			t = int(temp[0])
			entry = int(temp[0])
			if ( t < 300):
				t = "ROOM" + str(temp[0])
			del temp[0]
			actionwords = temp
			for actionnumber in actionwords:
				a = int(actionnumber)
				t = roomtable[roomname].traveltable
				t[a] = entry
				roomtable[roomname].redoarray(t)
	# Section 4 section 4
	# Each word matches a number. Some numbers have more than one
	# word. So, the key is the word. 
	if ( section == 4 ):
		if ( len(temp) > 1 ):
			word = temp[1]
			inputs[word] = temp[0]

	# Section 5 section 5 Object Descriptions - TBD
	# 
	if ( section == 5 ):
		if ( len(temp) > 1 ):
			number = temp[0]
			message = temp[1]

	# Section 6 section 6
	#
	# Multiple lines can happen for a given number, so set up something to
	# concatenate a string
	# 1(tab)stuff about a place
	# 2(tab)more stuff about a place
	if ( section == 6 ):
		if ( len(temp) == 2 ):
			m = str(temp[0])
			if m in amsg:
				if ( amsg[m] ):
					amsg[m] = amsg[m] + " " + temp[1]
			else:
				amsg[m] = temp[1]

	# Section 7 section 7
	#
	# This could also be part of the objects class
	if ( section == 7 ):
		if ( len(temp) > 1 ):
			objectnumber = temp[0]
			initiallocation = temp[1]
			itemlisttable[objectnumber] = objectnumber
			itemtable[objectnumber] = Item(objectnumber,initiallocation,"")
			item = itemtable[objectnumber]
			if ( len(temp)>2 ): 
				item.moveable = False
				if ( temp[2] < 0 ):
					pass
				else:
					item.secondlocation = temp[2]
					pass

	# Section 8 section 8
	if ( section == 8 ):
		if ( len(temp) > 1 ):
			actionverbnumber = temp[0]
			defaultmessageindex = temp[1]
		#index of default message (see section 6)


	# Section 9 section 9
	if ( section == 9 ): #liquidassets
		if ( len(temp) > 1 ):
			number = temp[0]
		#up to 20 location numbers
		#condition bits
	if (x[0] == '-' and x[1] == '1'): # separates sections, somewhat variable
		section += 1
		ROOMNAME = "ROOM0" #Reset the room number

# Done with the file. Close it.
textfiletoread.close()
#END READING FILE


def getlocationtable():
	return roomtable

def getlocationlisttable():
	return roomlisttable

def getitemlisttable():
	return itemlisttable

def getinputs():
	return inputs

def getitemtable():
	return itemtable

def getamsg():
	return amsg


