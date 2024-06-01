#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      smasherop
#
# Created:     05-08-2023
# Copyright:   (c) smasherop 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("welcome to bmi calculatorc!")
weight=float(input("what is your weight in kg? \n"))
height=float(input("what is your height in m?  \n"))

Bmi_cal=round (weight/(height)**2)
print(Bmi_cal)

if(Bmi_cal<18.5):
    print("Your bmi is 18.5 You are a underweight")
elif(Bmi_cal<25):
    print("You are a normal weight ")

elif(Bmi_cal<30):
    print("You are over weight")

elif(Bmi_cal<35):
    print("You are obese")


else:
    print("you are a clinically obese")
