#!/usr/bin/python
# actiondictionary.py
# Directions to go. If valid_direction[something], then its a direction.
#"ROOM1" : [0,"UP","DOWN","NORTH","SOUTH","EAST","WEST","NW","NE","SW","SE","OBJECTS_IN_ROOM"],
valid_direction = { 
	"UP" : 1,
	"DOWN" : 2,
	"N" : 3,
	"NORTH" : 3,
	"S" : 4,
	"SOUTH" : 4,
	"E" : 5,
	"EAST" : 5,
	"W" : 6,
	"WEST" : 6,
	"NW" : 7,
	"NORTHWEST" : 7,
	"SW" : 8,
	"SOUTHWEST" : 8,
	"NE" : 9,
	"NORTHEAST" : 9,
	"SE" : 10,
	"SOUTHEAST" : 10
	}

valid_command = [
	"Q",
	"QUIT",
	"UP",
	"DOWN",
	"N",
	"NORTH",
	"S",
	"SOUTH",
	"E",
	"EAST",
	"W",
	"WEST",
	"NW",
	"NORTHWEST",
	"SW",
	"SOUTHWEST",
	"NE",
	"NORTHEAST",
	"SE",
	"SOUTHEAST"
	]

