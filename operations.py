from datetime import datetime
from read import *
from write import *

def buyoperationPart(d):
        """THIS IS function FOR BUY TYPE"""
        Sold_Laptops = []
        Products_More = True

        name = input("Enter your name: ")
        print("\n")

        while Products_More== True:
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N     \t\t Product name    \t\t  Brand \t \t Price \t\t  Quantity  \t\t Processor \t\t Graphics Card")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


            table()

            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" )
        
            print("\n")

            s = False
            while s == False:
                try:
                    Pur_ID = int(input("Enter the ID of laptop you want to purchase: "))
                    
                

                # Valid ID
                    while Pur_ID <= 0 or Pur_ID > len(d):
                        print("Please provide valid laptop ID!")
                        print("\n")

        
                    print("To generate bill, please provide the details: ")
                    

                    s = True
                
                except:
                    print("No string allowed")
            #print("--------------------------------------------------------------------------------------------------------------------------------------")
            print("\n")
            

            
            phonenumber = input("Enter your phone number: ")
            print("\n")

            
            print("\n")

            s = False
            while s == False:
                try:
                    CustomerQuantity = int(input("Enter the quantity of laptop you want to purchase: "))
                    
                        
                    print("\n")
                    # Valid Quantity

                    DQuant = d[Pur_ID][3]
                    while CustomerQuantity <= 0 or CustomerQuantity > int(DQuant):
                        print("Dear user, the quantity you've asked for is not available right now.")
                        print("\n")
                        CustomerQuantity = int(input("The quantity of the chosen laptops you want to purchase: "))
                    

                

                    print("\n")

                        #
                    d[Pur_ID][3] = int(d[Pur_ID][3]) - int(CustomerQuantity)

                    file = open("file.txt", "w")

                    for values in d.values():
                            file.write(str(values[0])+ "," +str(values[1])+ "," +str(values[2])+ "," +str(values[3])+ "," +str(values[4]+ "," +str(values[5])))
                            file.write("\n")
                    file.close()
                    
                    s= True
                except:
                    print("No string allowed")  

            #
            ProductName = d[Pur_ID][0]
            QuantitySelected = CustomerQuantity
            UnitPrice = d[Pur_ID][2]
            Selected_Quantity_Price = d[Pur_ID][2].replace("$", '')
            Total_Price = int(Selected_Quantity_Price) * int(QuantitySelected)
            Graphics_card = d[Pur_ID][5]

            Sold_Laptops.append([ProductName, QuantitySelected, UnitPrice, Total_Price, Graphics_card])

            Request_By_Costumer = input("Do you want to continue (Y/N)?").upper()
            print("\n")
        
            if Request_By_Costumer == "Y":
                Products_More = True
            else:
                total = 0
                shipping_Cost = 10
                
                for i in Sold_Laptops:
                    total += int(i[3])
                Price_Before_VAT = total + shipping_Cost

                dateandtime = datetime.now()
                x = str(dateandtime).split(" ")
                s = "_".join(x)
                y = s.replace(":","_")

                printbuy(name, phonenumber, dateandtime, Sold_Laptops, total, shipping_Cost, Price_Before_VAT)


                
                billbuy(name,y,phonenumber,dateandtime,Sold_Laptops,total,shipping_Cost, Price_Before_VAT)
                Products_More = False


def selloperationPart(d):
        Sold_Laptops = []
        Products_More = True

        while Products_More== True:
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N      \t Product name           \t  Brand \t \t Price \t\t  Quantity  \t\t Processor \t\t Graphics Card")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


            file = open("file.txt", "r")
            a = 1
            for line in file:
                print(a, "\t\t" + line.replace(",", "\t\t"))
                a = a + 1
            print("----------------------------------------------------------------------------------------------------------------------------------" )
            file.close()
            print("\n")

            Pur_ID = int(input("Enter the ID of laptop you want to purchase: "))
            print("\n")

            # Valid ID
            while Pur_ID <= 0 or Pur_ID > len(d):
                print("Please provide valid laptop ID!")
                print("\n")

                Pur_ID = int(input("Enter the ID of laptop you want to purchase: \n"))

        
            
            name = "Hawk Store"
            print("\n")
            
            phonenumber = 9849535537
            print("\n")

            
            print("\n")

            CustomerQuantity = int(input("Enter the quantity of laptop you want to purchase: "))
            print("\n")
            # Valid Quantity

            DQuant = d[Pur_ID][3]
            while CustomerQuantity <= 0 or CustomerQuantity > int(DQuant):
                print("Dear user, the quantity you've asked for is not available right now.")
                print("\n")
                DQuant = int(input("Enter the quantity of the laptops you want to purchase: "))
            print("\n")

                #
            d[Pur_ID][3] = int(d[Pur_ID][3]) + int(CustomerQuantity)

            file = open("file.txt", "w")

            for values in d.values():
                    file.write(str(values[0])+ "," +str(values[1])+ "," +str(values[2])+ "," +str(values[3])+ "," +str(values[4])+ "," +str(values[5]))
                    file.write("\n")
            file.close()

            #
            ProductName = d[Pur_ID][0]
            QuantitySelected = CustomerQuantity
            UnitPrice = d[Pur_ID][2]
            Selected_Quantity_Price = d[Pur_ID][2].replace("$", '')
            Total_Price = int(Selected_Quantity_Price) * int(QuantitySelected)
            Price_After_VAT=(Total_Price*0.13)
            Graphics_card = d[Pur_ID][5]

            Sold_Laptops.append([ProductName, QuantitySelected, UnitPrice, Total_Price, Graphics_card])

            Request_By_Costumer = input("Do you want to continue (Y/N)?").upper()
            print("\n")
        
            if Request_By_Costumer == "Y":
                Products_More = True
            else:
                total = 0
                shipping_Cost = 10
                
                for i in Sold_Laptops:
                    total += int(i[3])
                Price_Before_VAT = total + shipping_Cost
                dateandtime = datetime.now()
                x = str(dateandtime).split(" ")
                s = "_".join(x)
                y = s.replace(":","_")

                printsell(name, phonenumber, dateandtime, Sold_Laptops, total, shipping_Cost, Price_Before_VAT)


                billsell(name,y, phonenumber, dateandtime, Sold_Laptops, total, shipping_Cost, Price_Before_VAT)
                Products_More = False
