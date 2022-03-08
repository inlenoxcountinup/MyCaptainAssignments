"""
Writing a python program for printing fibonacci numbers

The Fibonacci formula is given as, Fn = Fn-1 + Fn-2, where n > 1.

The Fibonacci sequence, in simple terms, 
says that every number in the Fibonacci sequence
 is the sum of two numbers preceding it in the sequence.

"""
#Creating a function to print the numbers using recursion.

def fibonacci(n):
    if n<=1:
        return n
    
    else:
        return(fibonacci(n-1)+fibonacci(n-2))


#Entering the nth term or letting the user input the number of terms they want it to display

n_terms=20    

#or n_terms=int(input("Enter the number of terms:")) can be used too!       

print("The Fibonacci numbers are:")
for i in range(n_terms):
    print(fibonacci(i))





""" 
Alternate Method


fn=0
fn2=1
count=0

n_terms=20 

#or n_terms=int(input("Enter the number of terms:")) can be used too!
print("The Fibonacci numbers are:")
while count<n_terms:
    print(fn)
    fnth=fn+fn2
    fn=fn2
    fn2=fnth
    count+=1     

 """   

