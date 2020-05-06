#coding:utf-8
import sys   
sys.setrecursionlimit(100000)

scoreList = [1, 5, 11]
# scoreList = [11, 5, 1]
scoreDict = {}
path = []
def getMinNum(target):
    global path
    if target in scoreDict:
        return scoreDict[target]

    print(target)
    if target in scoreList:
        scoreDict[target] = 1
        return 1
    numDict = {}

    for i in range(len(scoreList)):
        if target - scoreList[i] < 0:
            continue
        numDict[getMinNum(target - scoreList[i])] = scoreList[i]
    numList = list(numDict.keys())
    num = min(numList) + 1
    scoreDict[target] = num
    path.append(numDict[num - 1])
    return num


target = 100
num = getMinNum(target)
print(num)
print(path)