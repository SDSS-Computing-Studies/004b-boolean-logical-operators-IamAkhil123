#! python3
print("enter a number")
x = input()
if float(x) > 0.9759 and float(x) < 1.016:
  print ("That is within normal Earth orbit.")
else:  
    if float(x) < 0.9759 or float(x) > 1.016:
     print ("That is not within normal Earth orbit.")

"""
Open the file called task1.py
The Earth maintains an orbit where it's closest distance to \
the sun is 0.9759 AU and it's furthest distance to the sun is \
1.016 AU. \
Ask the user to enter a number. \
Tell them if the number is between 0.9759 and 1.016.\
(2 points) 
"""

"""
l
The Earth maintains an orbit where it's closest distance to  
the sun is 0.9759 AU and it's furthest distance to the sun is 
1.016 AU. 
Ask the user to enter a number. 
Tell them if the number is between 0.9759 and 1.016.
(2 points)

Inputs:
a number (float)

Outputs:
That is within normal Earth orbit.
That is not within normal Earth orbit.


Example:
Enter the distance of the Earth in AU: 9.4
That is not within normal Earth orbit.

Enter the distance of the Earth in AU: 1.011
That is within normal Earth orbit.

"""