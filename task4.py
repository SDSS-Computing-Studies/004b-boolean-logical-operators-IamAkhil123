#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ['Guile', 'Blanka', 'Christine', 'Carol', 'Richard', 'Daniel', 'Chun-Li']
x = input("enter your name")
if (x == VIPNames[0]) or (x == VIPNames[1]) or (x == VIPNames[2]) or (x == VIPNames[3]) or (x == VIPNames[4]) or (x == VIPNames[5]) or (x == VIPNames[6]):
   print("Hi",x + "!","You are a VIP!")
else:
   print("You are not a VIP")
