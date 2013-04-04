#!/usr/bin/python
#
# The fibonacci sequence 0, 1, 1, 2, 3 etc onto a bazillion.
#
# Since this can go on forever, let's stop at 10

a = 0
b = 1
c = 0

print a,
while ( c < 10):
	x = a  + b
	a = b
	b = x
	print " " + str(x),
	c = c + 1

print ""

# How about recursively?

def fib(a,b,x):
	if x > 9:
		return
	c = a + b
	print " " + str(c),
	a = b
	b = c
	x = x + 1
	fib (a,b,x)

print ""
fib (0,1,0)
