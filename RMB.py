#coding:utf-8
import sys   
sys.setrecursionlimit(100000)

scoreList = [1, 5, 11]
# scoreList = [11, 5, 1]
scoreDict = {}
path = []
def getMinNum(target):
    if target in scoreDict:
        return scoreDict[target]

    print(target)
    if target in scoreList:
        scoreDict[target] = 1
        return 1
    numList = []
    for i in range(len(scoreList)):
        if target - scoreList[i] < 0:
            continue
        numList.append(getMinNum(target - scoreList[i]))
    num = min(numList) + 1
    scoreDict[target] = num
    return num


target = 100
num = getMinNum(target)
print(num)