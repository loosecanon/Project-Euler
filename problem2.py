import math
sum = 0
i = 1
lastI = 1
while i<4000000:
    tmp = lastI #calculate next fibonacci number
    lastI = i
    i += tmp
    if i %2 == 0: # if even
        sum += i
        print("added number to sum")
        print(i)

print("Sum = ")
print(sum)
