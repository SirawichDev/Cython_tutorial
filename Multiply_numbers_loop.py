import numpy as np
import os

x=1
Cross = 1
number = int(input("Enter Number:"))
loop = int(input("Enter Loop:"))

while x<=loop :
    Cross *=number
    x+=1

print ("multiply result is :",Cross)
