import math
import fileinput
#create array of the digits of the number
grid = [[]]

def findResult(s, t): # return results table for a given X,Y pair
    result = [[1,1,1],[1,0,1],[1,1,1]]
    #print("call to findResult, s = ", s, " t = ", t)
    for d in range(0,4):
        #print("d = ", d)
        if s-d > 0:
            result[0][1] *= grid[s-d][t]
            if t-d > 0:
                result[0][0] *= grid[s-d][t-d]
                result[1][0] *= grid[s][t-d]
            if t+d < 20:
                result[0][2] *= grid[s-d][t+d]
        if t+d < 20:
            result[1][2] *= grid[s][t+d]
        if s+d < 20:
            result[2][1] *= grid[s+d][t]
            if t-d > 0:
                result[2][0] *= grid[s+d][t-d]
            if t+d < 20:
                result[2][2] *= grid[s+d][t+d]
        if s == 8:
            if t == 11:
                print("result table = ", result, " d = ", d)
    return result

textFile = open("grid.txt", "r")
i = 0
tmp = textFile.readline()
while(tmp != ""):
    tmp = tmp.rstrip("\n")
    #print("tmp = ", tmp)
    #print("I =: ", i)
    grid[i] = [int(x) for x in tmp.split(" ")]
    #print("grid line: ", i, " is ", grid[i])
    i+=1
    grid.append([])
    tmp = textFile.readline()
result = [[0,0,0],[0,0,0],[0,0,0]]
biggest = 0
oops = 0
#for each cell in the "interior" of the grid, check each direction for the biggest number
for s in range(0, 20):
    for t in range(0,20):
        result = findResult(s,t)
        for k in range(0,3):
            for r in range(0,3):
                if result[r][k] > biggest:
                    biggest = result[r][k]
                    print("result table = ", result)
                    print("Biggest result so far = ", biggest, " at X = ", t, " and Y = ", s)
print("absolute biggest = ", biggest)                

