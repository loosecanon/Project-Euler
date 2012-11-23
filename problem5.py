import math
num = 2520 #smallest number divisible by 1-10 inclusive
for i in range(1,21):
    print("num = ", num)
    print("i = ", i)
    print("num%i = ", num%i)
    if num%i != 0:
        tmp = i
        for j in range(1,tmp):
            if(tmp%j == 0): #if i is divisible by j, divide j out of i for addition
                print("tmp = ", tmp)
                print("j = ", j)
                tmp/=j
        num*=tmp
                
print("Smallest number = ")
print(num)
    
