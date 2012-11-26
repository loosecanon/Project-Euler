import math
from array import *

numbers = []
for i in range(0,2000000):
    numbers.append(1)

for j in range(2, 2000000):
    k=j
    k+=j
    while k<2000000:
        numbers[k]=0
        k+=j

sum = 0
for l in range(2,2000000):
    if numbers[l] == 1:
        #print("prime: ", l)
        sum+=l
print("sum = ", sum)
