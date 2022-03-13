"""
writing a python program to create a function called most_frequent
that takes a string and prints the letters in decreasing order
of frequency.

"""

word=str(input("Input: \nPlease Enter a String - ")) # variable created for getting the word from the user

# creating the function 
def most_frequent(a):
    d=dict() # empty dictionary created
    for i in a:        # running a for loop
        key_d=d.keys() # assigning dictionary keys to a variable
        if i in key_d: # checking for condition
            d[i]+=1    # adding +1 if the condition is satisifed 
        else:
            d[i]=1
    return d

dict_new=most_frequent(word) # new variable created & fucntion is used and the parameter is set as thr "word" variable 

sort_dict_new={} # new empty dictionary for sorting

sort_dict_new_keys=reversed(sorted(dict_new, key=dict_new.get)) # sorting the keys of the dictionary in descending order

for x in sort_dict_new_keys: # running a loop 
    sort_dict_new[x]=dict_new[x] # assigning empty dict - "sort_dict_new" to original dictionary (sorted)

finaldict=sort_dict_new # new variable created to assign final sorted dictionary  

print(word)

print("Output:")

for n in finaldict:
    print(n, "=", finaldict[n]) #running a loop to access keys along with its values
    





