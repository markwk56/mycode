#!/usr/bin/env python3

op_list = ["a", "s", "d", "m"]


print("Welcome to using the AWESOME Python Calculator :) ")

print("You will be ask to enter two number and what operation you wnat performed. \n\n")



while True:
    try:
        num1 = float(input("Enter your first number: "))
        break
    except:
        print("your first entry was not a number. Please try again")
      
    

while True:
    try:
        num2 = float(input("Enter your second number: "))
        break
    except:
        print("Your second entry was not a number.  Please try again. ")

operation = input("Enter the operation with the character within the parens: (a)dd, (s)ubtract, (d)ivide, (m)ultiply: ").lower()



def add(num1,num2):
    return (num1+num2)


def sub(num1,num2):
    return (num1-num2)


def div(num1,num2):
    return (num1/num2)

def mult(num1,num2):
    return(num1*num2)

while True:
    if operation in op_list:
        if operation == "a":
            print("The result of your addition is: ", add(num1,num2))
            break
        elif operation == "s":    
            print("The result of your subtraction is: ", sub(num1,num2))
            break
        elif operation == "d" and num2 == 0:
            print("You tried to divie by 0 which is not allowed. ")
            break
        elif operation == "d":
            print("The result of your division is: ", div(num1,num2))
            break
        else:
            print("The result of your multiplication is: ", mult(num1,num2))
            break
    else:
        print("You entered an incorrect operation\n")
        operation = input("Please try again: (a)dd, (s)ubtract, (d)ivide, (m)ultiply: ").lower()

print("Thankyou for using the calculator. \n")



   
