#this import is done to get aceess to few other math functions
# this function is gonna grab bunch of diff math functions
# math in the below statement is called MODULE

from math import *

# floor grabs the lowest  value. it chops off the decimal value
print (floor(3.7))

#(ceil) does the exact opposite of floor. it rounds the number , no matter what
print (ceil(3.7))

#(sqrt)- finds the sqaure root of two given numbers
print(sqrt(36))

# copysign(x,y) - returns x with sign of y
print(copysign(3,-6))

# fabs(x)- returns absolute value of x
print(fabs(-3))

# factorial(x)-	Returns the factorial of x
print(factorial(5))

#fmod(x, y)-Returns the remainder when x is divided by y
print(fmod(4,3))

#frexp(x)-	Returns the mantissa and exponent of x as the pair (m, e)
print(frexp(2))

#fsum(iterable)- Returns an accurate floating point sum of values in the iterable
# here we pass some value which is iterable like arrays, list.
# the function returns a floating point number
print(fsum(range(10)))

#isfinite(x)-	Returns True if x is neither an infinity nor a NaN (Not a Number)
print(isfinite(3))

#isinf(x)	Returns True if x is a positive or negative infinity
print(isinf(3))