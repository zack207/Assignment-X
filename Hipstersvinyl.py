#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:  Zack LeBlanc 
Program Title: Hipsters vinyl records 
Description: Customers order details
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
#welcome message
   
    print("welcome to hipsters vinyl")

    #INPUT ask customer for info
    customerName = input(" your name ")
    Delkm = float(input(" enter the distance in kilometer "))
    costofRecords = float (input(" enter the cost of the records "))

    #PROCESS
    Deliverycost = 15 * Delkm
    costofpurchase = costofRecords * .14 + costofRecords
    Totalcost = Deliverycost + costofpurchase

    #OUTPUT
    print("Delivery Cost:${0:.2f}".format(Delkm))
    print("Purchase Cost:${0:.2f}".format(costofpurchase))
    print("Total Cost:${0:.2f}".format(Totalcost))  
  
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()