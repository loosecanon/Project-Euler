import math
numFactors = 0
number = 1
adder = 2
def factors(num):
    fac = 0
    tl = []
    for x in range(2,int(math.sqrt(num))):
        s,r = divmod(num,x)
        if r == 0:
            tl.append(x)
            tl.append(s)
    return len([1, number] + tl)
    
while numFactors < 500:
    number += adder
    adder += 1
    numFactors = factors(number)
print("number of factors: ", numFactors, "for number ", number)
