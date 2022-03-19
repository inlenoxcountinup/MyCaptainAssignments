import csv

def writeinto_csv(info_stu):
    with open("Students Information.csv", "a", newline='') as main:
        writer=csv.writer(main)
        if main.tell()==0:
            writer.writerow(["Name","Age","Phone Number", "Email-ID"])

        writer.writerow(info_stu)

if __name__ == "__main__":
    runsys = True
    Sr_No = 1

    while(runsys):
        stu_infovar1 = input("Enter Student No.{} Name:".format(Sr_No))
        stu_infovar2 = input("Enter Student No.{} Age:".format(Sr_No))
        stu_infovar3 = input("Enter Student No.{} Phone Number:".format(Sr_No))
        stu_infovar4 = input("Enter Student No.{} Email-ID:".format(Sr_No))
        stu_allvars  = [stu_infovar1, stu_infovar2, stu_infovar3, stu_infovar4]

        print("The Entered Information is as follows: \nName: {}\nAge: {}\nPhone Number: {}\nEmail-ID: {}".format(stu_infovar1, stu_infovar2, stu_infovar3, stu_infovar4))

        confirmation = input("Is the information entered correct? (y/n)")

        if confirmation == "y":
            writeinto_csv(stu_allvars)
            print("{}'s Details Succesfully Registered!".format(stu_infovar1))

            addcheck = input("Do you want to add information for another student? (y/n)")
            
            if addcheck == "y":
                runsys = True
                Sr_No += 1
            
            elif addcheck == "n":
                runsys = False

        elif confirmation == "n":
            print("\nPlease Re-Enter the Values!")
