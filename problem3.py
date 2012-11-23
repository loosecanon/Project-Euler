import math
num = 600851475143
largest = 1 # largest factor found in search space
for i in range(1, math.floor(math.sqrt(600851475143))):
    if num%i == 0:
        largest = i
        num = num/largest
        print('found new factor: ')
        print(i)

print('largest factor: ')
print(largest)
