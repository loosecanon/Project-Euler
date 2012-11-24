import math
from array import *
#create array of the digits of the number
number = array("I")
textFile = open("number.txt", "r")
for i in range(0,1000):
    number.append(int(textFile.read(1)))
    #print("Digit i = ", number[i])
#run through array, looking for the largest product of 5 consecutive digits
index = 0
bigProduct = 0
for j in range(0, 956):
    product = 1
    for k in range(j, j+5):
        product *= number[k]
    if(product > bigProduct):
        bigProduct = product
        index = j
print("biggest product = ", bigProduct, " at index: ", index)
