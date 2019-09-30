#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:  Zack LeBlanc
Program Title:  
Description: 
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #INPUT ask user to fill fields
    tons = float(input(" enter number of tons "))
    stones = float(input(" enter number of stones "))
    ounces = float(input(" enter number of ounces "))
    pounds = float(input(" enter number of lbs "))
   
    #PROCESS formula giving in word document to figure out what each are
    totalounces = 35840 * tons + 224 * stones + 16 * pounds + ounces
    totalkilos = int(totalounces / 35.274)
    metrictons = int(totalkilos / 1000)
    kilos = (metrictons) * 1000
    grams = (kilos) * 1000  

    #OUTPUT
    print(" the metric weights are ")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()