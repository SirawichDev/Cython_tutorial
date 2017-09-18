import numpy as np
import time

x=1
Cross = 1
number = int(input("Enter Number:"))
loop = int(input("Enter Loop:"))

while x<=loop :
    Cross *=number
    x+=1


start_time = time.time()

