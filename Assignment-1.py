"""
MyCaptainAssignment
@author: Anurag
"""


#Creating a Python program which accepts the radius of a circle from the user and computes area
radius=float(input("Input the radius of the circle:"))
area=3.14*radius*radius
print(radius)
print("The area of the circle with radius", radius, "is:", area)

#Creating a Python program to accept a filename from the user and printing the extension of the file
file=input("Input the Filename:")
extension=file.split(".")
print("The extension of the file is:", extension[1])

