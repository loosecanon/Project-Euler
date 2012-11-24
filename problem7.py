import math
#compute 10001st prime number
i = 1 # first prime
num = 2 #number under examination storage variable
while i < 10001:
    num+=1
    for j in range(2,num):
        #print("j = ", j, " num = ", num," i = ", i)
        if num%j == 0:
            break
    else:
        i+=1
print("100001st prime = ", num)
