# Writing a python program to print all positive numbers in a range/list

list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]

# creating an empty list
list = []

# number of elements as input
n = int(input("Enter number of elements for creation of a list:"))

#iterating till the range
for i in range(0, n):
    add_element = int(input("enter element:")) #enter the element and hit enter to add another one
    
    #adding the element
    list.append(add_element)  

print("The list is created!")     
print(list)

print("Positive integers in this list are:")

# running a loop to print the positive numbers from the list
for num in list:
    if num>1: #checking for a condition
        print(num)
    


""""
working with already created lists

"""
print("Positive integers in list1 are:")
# running a loop to print the positive numbers from the list
for num in list1:
    if num>1: #checking for a condition
        print(num)


print("Positive integers in list2 are:")
# running a loop to print the positive numbers from the list
for num in list2:
    if num>1: #checking for a condition
        print(num)


