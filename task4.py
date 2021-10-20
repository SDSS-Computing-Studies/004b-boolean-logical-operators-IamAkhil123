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
VIPNames = ("Guile" or "Blanka" or "Christine" or "Carol" or "Richard" or "Daniel" or "Chun-Li")
print("enter your name")
x = input()
if (x == VIPNames):
   print("Hi!",x,"you are a VIP!")
else:
   print("you're not a VIP")


