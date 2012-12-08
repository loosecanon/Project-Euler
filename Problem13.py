import math
from uuid import int_
from lib2to3.fixer_util import Number

numberArray = [[]]
textFile = open("numbers.txt","r")
tmp = textFile.readline()
lines = 0
#read in numbers
while tmp:
    print("tmp = ", tmp)
    i = 0
    for char in tmp:
        numberArray[lines].append([])
        #print("char = ", char, "i = ", i, "lines = ", lines)
        numberArray[lines][i] = char
        i+=1
    tmp = textFile.readline()
    lines+=1
    numberArray.append([])
#number array populated, now add numbers and insert into result array
results = [] 
carry = 0
for i in range(0,50):
    subTotal = carry
    for j in range(0,100):
        #print("i = ", i, "number = ", numberArray[j][49-i])
        from ctypes.wintypes import INT
        subTotal += int(numberArray[j][49-i])
    print("subtotal = ", subTotal)
    d,r = divmod(subTotal, 10)
    results.append("")
    results[i] = r
    carry = d
    print("r = ", r, " carry = ", carry)
while carry > 0:
    i+=1
    d,r = divmod(carry, 10)
    results.append("")
    results[i] = r
    carry = d
results.reverse()
for ch in results:
    print(ch, end='')
