#! python3

x = input("Enter an integer")
y = input("Enter an interger")
z = input("Enter an interger")
x = int(x)
y = int(y)
z = int(z)
c = max(x,y,z)
a = min(x,y,z)
my_list = (x,y,z)
b = my_list[int(len(my_list)/2)]
g = str(a) + "," + str(b) + "," + str(c)
if a ** 2 + b ** 2 == c ** 2:
 print(g, "form a Pythagorean triple")
else:
 print(g, "do not form a Pythagorean triple")

"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
