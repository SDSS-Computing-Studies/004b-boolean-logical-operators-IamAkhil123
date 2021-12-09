#! python3

x = input("Enter a number")

p = float(x) % 6
y = p == 0
l = float(x) % 8 
y2 = l == 0

if y == True and y2 == False:
 print(x, "is frue")
else:
 print(x, "is not frue")

"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

