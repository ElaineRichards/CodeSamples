#!/usr/bin/python
# Classic interview question. Take a list of 100 integers. If the integer
# is divisible by 3, print "Fizz". If the integer is divisible by 5, print
# "Buzz". If the integer is divisible by 15, print "FizzBuzz". Otherwise,
# print the integer.
#

i = 0
while i < 101:
	i += 1
	if (i%15 == 0 ):
		print "FizzBuzz"
		continue
	if i%3 == 0:
		print "Fizz"
		continue
	if i%5 == 0:
		print "Buzz"
		continue
	print i
