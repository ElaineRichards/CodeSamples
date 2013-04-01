#!/usr/bin/python
#
# Reverse a String
#
# One interview question I saw on the internet was to recursively reverse
# a string, because I guess you can't use some simple library. I don't know
# the O log N notation for this one. 
#

old = "cow"
new = ""
l = len(old)

def reverse_string(s,n,l):
	if ( l < 1 ):
		return n
	else:
		l = l - 1
		n = n + s[l] #HERE
		return reverse_string(s,n,l)
	print "should not get here"

new = reverse_string(old,new,l)
print new
