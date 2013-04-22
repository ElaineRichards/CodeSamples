#!/usr/bin/python
import string
import sys

""" This is an object oriented version of "The Colossal Cave Adventure",
    which just seemed like a goofy and fun way of teaching myself how
    to write Python in general and objects in specific.

    readit.py reads the original tables (advent.dat) and loads that into
    data structures.

"""
from readit import Item
from readit import Location
from readit import getlocationtable
from readit import getlocationlisttable
from readit import getitemlisttable
from readit import getinputs
from readit import getitemtable
from readit import getamsg

action = "GO"
location = "ROOM1"

locationtable = getlocationtable()
inputs = getinputs()
inputarray = inputs.keys()
amsg = getamsg()

def figureoutwhattodo(actionnumber):
	print "inside figureoutwhattodo ",
	print actionnumber
	if ( actionnumber > 500 ):
		print "print a message from section 6"
		print amsg[actionnumber]
	m = y/1000
	n = y % 1000
	

# Initially, we're in "ROOM1" We print the description and mark it as
# having been visited. This means future messages are short, unless you
# type "LOOK" 

print locationtable[location].long_description
locationtable[location].visited = True
#
while ( action != "QUIT" ):
	input = raw_input("> ")
	action = str(input)
	action = action.upper()
	if ( action == "LOOK" ):
		print locationtable[location].long_description
		continue
	if (action not in inputarray):
		print "I don't understand that."
		continue
	actionnumber = int(inputs[action])
	if ( actionnumber < 300 ):
		print "actionnumber is less than 300 ",
		print actionnumber
		if ( locationtable[location].visited == False ):
			print locationtable[location].long_description
			locationtable[location].visited = True
		else:
			print locationtable[location].short_description
		n = locationtable[location].traveltable[actionnumber]
		if ( n == "i" ):
			print "You can't go there."
			continue
		if ( n < 300 ):
			nextroom = "ROOM" + str(n)
			print "nextroom is ",
			print nextroom
			location = nextroom
		else:
			figureoutwhattodo(n)
			print "N is not a room ",
			print n
	else:
		print "action number is greater than 299"
