"""
MyCaptainAssignment
@author: Anurag

"""

import csv # importing csv library

# creating a function to create a new csv file and entering the data that is obtained from the user
def writeinto_csv(info_stu):
    with open("Students Information.csv", "a", newline='') as main: # creation of the csv file
        writer=csv.writer(main) # writer class to enter data
        if main.tell()==0: # condition check to see if the file is empty
            writer.writerow(["Name","Age","Phone Number", "Email-ID"]) # adding the column names

        writer.writerow(info_stu)

if __name__ == "__main__":
    runsys = True # setting program condition as True to keep it running
    Sr_No = 1     # serial number of student

    while(runsys): # main prograrm
        stu_infovar1 = input("Enter Student No.{} Name:".format(Sr_No)) # requesting user to input the name
        stu_infovar2 = input("Enter Student No.{} Age:".format(Sr_No))  # requesting user to input the age
        stu_infovar3 = input("Enter Student No.{} Phone Number:".format(Sr_No))  # requesting user to input the phone number
        stu_infovar4 = input("Enter Student No.{} Email-ID:".format(Sr_No)) # requesting user to input the email ID
        stu_allvars  = [stu_infovar1, stu_infovar2, stu_infovar3, stu_infovar4] # created a list of all the variables above
           
        # displaying the information entered 

        print("The Entered Information is as follows: \nName: {}\nAge: {}\nPhone Number: {}\nEmail-ID: {}".format(stu_infovar1, stu_infovar2, stu_infovar3, stu_infovar4))

        # asking the user if the information that's entered by them is correct or not?
        
        confirmation = input("Is the information entered correct? (y/n)")  

        # checking for a condition, if the user confirms the info entered is correct or not
        
        if confirmation == "y":
            writeinto_csv(stu_allvars) # if yes, info is entered into csv file
            print("{}'s Details Succesfully Registered!".format(stu_infovar1)) # displaying a message showing the details are entered in the csv file

        # asking the user if they wish to add another student's details

            addcheck = input("Do you want to add information for another student? (y/n)")
            
            if addcheck == "y": # checking for the condition
                runsys = True # if they wish to enter another student's info, the program will keep running
                Sr_No += 1 # serial number value increased by 1 for a new entry
            
            elif addcheck == "n":
                runsys = False # if n is selected the program stops running 

        elif confirmation == "n": 
            print("\nPlease Re-Enter the Values!") # if the information is incorrect, the user has to re-enter the details
