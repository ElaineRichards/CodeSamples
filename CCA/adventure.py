#!/usr/bin/python
import string
import sys
from classes import Location
from classes import assignvalue
from locationlist import rooms
from locationdictionary import locationinfo
from actiondictionary import valid_command
from actiondictionary import valid_direction

""" This is an object oriented version of "The Colossal Cave Adventure",
    which just seemed like a goofy and fun way of teaching myself how
    to write Python in general and objects in specific.

    The original author had a different way of representing the game
    entirely (I think it was a graphing problem). So, this is not an
    exercise in doing exactly what he did. This is just something for my
    Python portfolio.

    Yes, it is screamingly time consuming to figure out all the directions.
"""

action = "GO"
roomkey = "ROOM1"

where_i_am = assignvalue(roomkey)
print where_i_am.r_description
while ( action != "QUIT" ):
# NOTE: Yes, I'm using Python 2.7.
	input = raw_input("> ")
	action = str(input)
# NOTE: action = action.upper is incorrect , use action.upper()
	action = action.upper()
# NOTE: import sys and use sys.exit to exit from main program

	if action in valid_command:
		if action == "QUIT" or action == "Q":
			sys.exit("Thank you for playing")
		vdir = valid_direction[action]
		if ( vdir ):
			nextroom = locationinfo[roomkey][vdir]
			if ( nextroom == "CANTGO" ):
				print "You can't go that way"
			else:
				where_i_am = assignvalue(nextroom)
				print where_i_am.r_description
	else:
		print "I don't understand you."


