import math
#find pythagorean triplet such that A+B+C = 1000 and A**2 + B**2 = C**2

for a in range(2,999):
    for b in range(2, 999):
        c = math.sqrt(a**2 + b**2)
        if(a+b+c == 1000):
            print("Found a solution: a = ", a, " b = ", b, " c = ", c)
            print("product = ", a*b*c)
            break
            
