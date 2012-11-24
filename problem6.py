import math
#compute sum of squares 0-100
sumSquares = 0
for i in range(0,101):
    sumSquares+= i**2
print("Sum of squares = ", sumSquares)

#compute square of sum of 0-100
sum = 50*101 #1+100 + 2+99 . . .
sumSquared = sum**2
print('Sum = ', sum)
print("sum squared = ", sumSquared)
print("Difference: ", sumSquared-sumSquares)
