#! python

"""
Note:  Many languages have a problem when dealing with floating point
decimals, and python is no exception.
Sometimes, when finding the cube root of large numbers, like 729,
you may get 8.9999999999999999999998 instead of 9
To get around this, we can use the round() command
round() accepts 2 parameters, the number to be rounded, and how many decimals
a = round(3.999999999999998, 8) would round at the 8th decimal place, for example.
You don't want to round too early (ie to the nearest whole number) because that
might be too inaccurate.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.

Enter a number: 64
64 is both a perfect square and a perfect cube.
"""
import math 
print("enter a number")
number = input()
x = int(number)
if(int(round(x ** (1. / 3))) ** 3 == x):
  print(number, "It is a perfect cube")
number = int(x)
root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print(number, "is only a perfect square.")
    if (int(round(x ** (1. / 3))) ** 3 == x) and int(root + 0.5) ** 2 == number:
      print( number, "is both a perfect square and a perfect cube.")






