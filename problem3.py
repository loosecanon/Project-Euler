import math
num = 600851475143
largest = 1 # largest factor found in search space
for i in range(1, math.floor(math.sqrt(num))):
    for x in range(2,i):
        if i%x == 0:
            break
    else:
        #print('found new prime:')
        #print(i)
        if num%i == 0:
            largest = i
            num = num/largest
            print('found new factor: ')
            print(i)

print('largest factor: ')
print(largest)
