#!/usr/bin/python
# Make sure there is a file called __init__.py in directory. This is empty
# Don't use "locationlist.py", just "locationlist"
#
# locationlist has the array of rooms, import that data structure
# locationdictionary has a dictionary of room information

from locationlist import rooms
from locationdictionary import locationinfo

class Location:
	def __init__(self, roomname, r_description, r_up, r_down, r_north, r_south, r_east, r_west, r_nw, r_ne, r_sw, r_se, r_objects ):
		self.roomname =  roomname
		self.r_description = r_description
		self.r_up = r_up
		self.r_down = r_down
		self.r_north = r_north
		self.r_south = r_south
		self.r_east = r_east
		self.r_west = r_west
		self.r_nw = r_nw
		self.r_ne = r_ne
		self.r_sw = r_sw
		self.r_se = r_se
		self.r_objects = r_objects

class Player:
	def __init__(self, whereami)
		self.whereami = whereami

#
# I can't seem to just feed the array into the __init__ for the class. That'll
# get figured out later.
#
def assignvalue(roomname):
	roomarray = locationinfo[roomname]
	thisthingie = Location( roomname, roomarray[0], roomarray[1], roomarray[2], roomarray[3], roomarray[4], roomarray[5], roomarray[6], roomarray[7], roomarray[8], roomarray[9], roomarray[10], roomarray[11])
	return thisthingie


anotherroom = assignvalue("ROOM2")
print anotherroom.r_description
