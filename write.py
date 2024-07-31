def printbuy(name, phone_number, dateandtime, laptop_sold, total, shipping_charge, grand_total):
    
            print("\n")
            print("\t \t \t \t \t \t \t HAWK STORE INVOICE")
            print("\n")
            print("\t \t \t \t \t Boudha , Kathmandu | Phone no: 987896543")
            print("\n")
            print("---- ")
            print("Product details: \n")
            print("-----")
            print("Customer's Name: "+ str(name))
            print("Contact number: "+ str(phone_number))
            print("Date and time of purchase: "+ str(dateandtime))
           
            print("\n")
            print("Purchase Details are: ")
            
            print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
            print("-")
            for i in laptop_sold:
                print(i[0], "\t\t\t" ,i[1], "\t\t\t " ,i[2], "\t\t\t " ,"$", i[3] )
           
            print("Your total is : $"+str (total))
            print("Your Shipping charge is : $", shipping_charge)
            print("Grand Total : $"+ str(grand_total))
            print("\n")
def billbuy(name,y,phone_number,dateandtime,laptop_sold,total,shipping_charge, grand_total):
        file= open(str(name)+"_"+str(y)+".txt", "w")
        file.write("\n")
        file.write("\t \t \t \t \t \t \t HAWK STORE INVOICE")
        file.write("\n")
        file.write("\t \t \t \t \t Chabahil, Kathmandu | Phone no: 98163332")
        file.write("\n" )
        file.write("\nCustomer's Name: " + str(name))
        file.write("\nContact number: " + str(phone_number))
        file.write("\nDate and time of purchase: " + str(dateandtime))
        file.write("\n" )
        file.write("\n")
        file.write("Purchase Details are: ")
        file.write("\n------------------------------------------------------------------------------------------------------------------------\n" )
        file.write("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        file.write("\n------------------------------------------------------------------------------------------------------------------------ \n" )


        for i in laptop_sold:
            file.write(str(i[0])+"\t\t\t "+str(i[1])+"\t\t\t\t\t\t "+str(i[2])+"\t\t\t\t\t\t\t"+"$"+str(i[3]) +"\n")


        file.write("-" )
        file.write("\nYour total is : $" + str(total))
        file.write("\nYour Shipping charge is : $ " +""+ str(shipping_charge) +"\n")
        file.write("\nGrand Total : $" + str(grand_total))
        file.write("\n")
        file.close()

def printsell(name, phone_number, dateandtime, laptop_sold, total, shipping_charge, grand_total):
        print("\n")
        print("\t \t \t \t \t \t \t Maanifacturer")
        print("\n")
        print("\t \t \t \t \t Chabahil , Kathmandu | Phone no: 1111111111")
        print("\n")
        print("---- ")
        print("Product details: \n")
        print("-----")
        print("Customer's Name: "+ str(name))
        print("Contact number: "+ str(phone_number))
        print("Date and time of purchase: "+ str(dateandtime))
        print("-")
        print("\n")
        print("Purchase Details are: ")
        print("-")
        print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        print("-")
        for i in laptop_sold:
            print(i[0], "\t\t\t" ,i[1], "\t\t\t " ,i[2], "\t\t\t " ,"$", i[3] )
        print("-")
        print("Your total is : $"+str (total))
        print("Your Shipping charge is : $", shipping_charge)
        print("Grand Total : $"+ str(grand_total))
        print("\n")

def billsell(name,y, phone_number, dateandtime, laptop_sold, total, shipping_charge, grand_total):
        file= open(str(name)+ str(y)+ "file.txt", "w")
        file.write("\n")
        file.write("\t \t \t \t \t \t \t HAWK STORE INVOICE")
        file.write("\n")
        file.write("\t \t \t \t \t Chabahil, Kathmandu | Phone no: 98163332")
        file.write("\n" )
        file.write("\nCustomer's Name: " + str(name))
        file.write("\nContact number: " + str(phone_number))
        file.write("\nDate and time of purchase: " + str(dateandtime))
        file.write("\n" )
        file.write("\n")
        file.write("Purchase Details are: ")
        file.write("\n------------------------------------------------------------------------------------------------------------------------\n" )
        file.write("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        file.write("\n------------------------------------------------------------------------------------------------------------------------ \n" )


        for i in laptop_sold:
            file.write(str(i[0])+"\t\t\t "+str(i[1])+"\t\t\t\t\t\t "+str(i[2])+"\t\t\t\t\t\t\t"+"$"+str(i[3]) +"\n")


        file.write("-" )
        file.write("\nYour total is : $" + str(total))
        file.write("\nYour Shipping charge is : $ " +""+ str(shipping_charge) +"\n")
        file.write("\nGrand Total : $" + str(grand_total))
        file.write("\n")
        file.close()

