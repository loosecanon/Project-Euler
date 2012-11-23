import math
largest = 0
for i in range(316,1000):
    for j in range(316,1000):
        num = i*j
        if(num % 10 == num//100000):
            #print("mod 10 and 100k")
            if((num%100)//10 == ((num%100000)//10000)):
                #print("mod 100 and 10k")
                if((num%1000)//100 == (num%10000)//1000):
                    print("num is palindrome")
                    print(num)
                    if(num > largest):
                        largest = num
print("Largest Palindrome:")
print(largest)
                    
