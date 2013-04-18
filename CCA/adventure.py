#!/usr/bin/python
import string
import sys

""" This is an object oriented version of "The Colossal Cave Adventure",
    which just seemed like a goofy and fun way of teaching myself how
    to write Python in general and objects in specific.

    The original author had a different way of representing the game
    entirely (I think it was a graphing problem). So, this is not an
    exercise in doing exactly what he did. This is just something for my
    Python portfolio. I am putting NOTE:s to myself as I learn Python.

    Yes, it is screamingly time consuming to figure out all the directions.
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
	if (action not in inputarray):
		print "I don't understand that."
		continue
	actionnumber = int(inputs[action])
	actionword = action
	if ( action == "LOOK" ):
		print locationtable[location].long_description
		continue
	if ( actionnumber < 300 ):
		if ( locationtable[location].visited == False ):
			print locationtable[location].long_description
			locationtable[location].visited = True
		else:
			print locationtable[location].short_description
			nextroom = locationtable[location].traveltable[actionnumber]
			if ( nextroom == "i" ):
				print "You can't go there."
			else:
				print "nextroom is " + nextroom
				location = nextroom
	else:
	# The action number is greater than 300, which means we are not moving.
		print "Placeholder for other action"
		print "actionnumber is ",
		print actionnumber
		print "actionword is " + actionword
#		if ( valid_direction.get(action)):
#			vdir = valid_direction[action] #vdir is integer
#			nextroom = locationinfo[roomkey][vdir]
#			if nextroom == "CANTGO":
#				print "You can't go in that direction!"
#			else:
#				where_i_am = assignvalue(nextroom)
#				print where_i_am.r_description
#	else:
#		print "I don't understand you."
#
#
