from datetime import datetime
from read import *
from operations import *
from write import *


 

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(" \t \t \t \t \t \t \t Welcome to The Hawk Store!")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print ("\n")


d=read1()


    
loop = True
while loop == True:
    print("1. Sell laptops to Customer")
    print("2. Purchase laptop from company")
    print("3. Exit")
    print("\n")
    s = False
    while s == False:
        try:
            u_i= int(input("Enter the option to continue: "))
            s = True
        except:
            print("No string allowed")

    print("\n")

    if u_i == 1:
        
        buyoperationPart(d)



                      

        

    elif u_i == 2:
        
        
        selloperationPart(d)



  

        print("\n")
        
    elif u_i == 3:
        loop = False
        print("Thank you for visiting our store!")
        print("\n")
    else:
        print("Your option", u_i, "does not match. try again.")
        print("\n")
