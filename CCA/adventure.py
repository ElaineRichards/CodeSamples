#!/usr/bin/python
# Pythonic modules
import string
import sys
# Note that it is sys.exit() <- don't forget the ()

""" This is an object oriented version of "The Colossal Cave Adventure",
    which just seemed like a goofy and fun way of teaching myself how
    to write Python in general and objects in specific.

    readit.py reads the original tables (advent.dat) and loads that into
    data structures.

"""
# Homebrewed modules
from readit import Item
from readit import Location
from readit import getlocationtable
from readit import getlocationlisttable
from readit import getitemlisttable
from readit import getinputs
from readit import getitemtable
from readit import getamsg
from readit import actionwords

# This just shows you where you are. If you already visited, it shows the
# short desecription. If you have not visited, it shows the long description.

def locationshow(locationtable,location):
	if locationtable[location].visited == False:
		print locationtable[location].long_description
		locationtable[location].visited = True
	else:
		print locationtable[location].short_description

# This is the exciting stuff. Still reading the notes in the Fortran original.
# All sorts of fun math going on here.
#
def interpretmotion(motion):
	m = motion/1000
	n = motion % 1000
	print "m the divided by 1000 is ",m
	print "n the modulo of 1000 is ",n
	if n > 500:
		print "message n - 500 from section 6 is printed"
		messagespot = n - 500
		print messagespot
	if motion < 300:
		return "MOTION"
	if motion < 500:
		print "computed goto"
	if motion > 500:
		messagenumber = motion - 500
		m = str(messagenumber)
		if amsg[m]:
			print amsg[m]
#
# This deals with section 4 - vocabulary
#
def dealwithvocabulary(actionnumber):
	print "inside dealwithvocabulary ",
	print actionnumber
	print "actionnumber",actionnumber
	#print amsg,items()
	# Divide the number by 1000
	# if m = 0, it's an motion word
	# if m=2, it's an action
	# if m=3, it's a special case
	# N mod 1000 is an index into section 6
	m = actionnumber/1000
	n = actionnumber % 1000
	print "Actionnumber is ",actionnumber,"and m is ",m
	if ( m == 0 ):
		print "It is a motion."
		print "specifies the conditions of the motion."
		print "It is unconditional."
	if ( m == 1 ):
		print "It is an object."
		print "Object description."
	#	print actionwords[m]
		print actionwords[n]
		print "There should be actionwords actionnumber"
	if ( m == 2 ):
		print "It is an action verb like carry."
	#	print actionwords[m]
		print actionwords[n]
		
	if ( m == 3 ):
		print "It is a special case word."
	n = actionnumber % 1000
	print "Modulo is", n
	if ( n > 500 ):
		print "message should be printed"
		print "person stays put"

# Initially, we're in "ROOM1" We print the description and mark it as
# having been visited. This means future messages are short, unless you
# type "LOOK" 
#
def main():
	action = "GO"
	location = "ROOM1"
	locationtable = getlocationtable()
	inputs = getinputs()
	inputarray = inputs.keys()
	amsg = getamsg()
	while ( action != "QUIT" ):
		locationshow(locationtable,location)
		input = raw_input("> ")
		action = str(input)
		action = action.upper()
		if ( action == "QUIT" ):
			continue
		if ( action == "LOOK" ):
			print locationtable[location].long_description
			continue
		if (action not in inputarray):
			print "I don't understand that. - not in input array"
			continue
		actionnumber = int(inputs[action])
		if ( actionnumber < 300 ):
			# You move
			n = locationtable[location].traveltable[actionnumber]
			if ( n == "i" ):
				print "n is ",n
				print "You can't go there."
				continue
			if ( n < 300 ):
				nextroom = "ROOM" + str(n)
				location = nextroom
			else:
				dealwithvocabulary(n)
				interpretmotion(n)
		else:
			dealwithvocabulary(actionnumber)
			#interpretmotion(actionnumber)
			print "action number is greater than 299"

if __name__ == '__main__':
	main()
