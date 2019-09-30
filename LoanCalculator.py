#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:  Zack LeBlanc
Program Title:  weekly loan calculator
Description: build a calculator to determine your weekly loan payment
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Input Loan amount, interest, and years owing

    loanamount = int(input(" enter loan amount: "))
    interest = float(input(" enter interest rate: "))
    yearsowing = int(input(" enter years owing: "))
    i = interest / 5200

    #PROCESS
    payment = (i / (1- (1 + i) ** (-52 * yearsowing)) * loanamount)

    #OUTPUT
    print(" your payment will be: {0:.2f}".format(payment))
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()