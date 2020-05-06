#coding:utf-8
import sys   
sys.setrecursionlimit(100000)

scoreList = [1, 5, 11]
# scoreList = [11, 5, 1]
scoreDict = {}
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

def getMinNumLoop(target):
    for i in range(min(scoreList), target + 1):
        if i in scoreList:
            scoreDict[i] = 1
            continue
        num = -1
        for score in scoreList:
            if i - score <= 0:
                continue
            print("%d:%d\n"%(i, num))

            if num == -1:
                num = scoreDict[i - score] + 1
                continue
            num = min(num, scoreDict[i - score] + 1)
        scoreDict[i] = num
        print("%d:%d\n"%(i, num))
    return scoreDict[target]

target = 100
num = getMinNumLoop(target)
print(num)
print(scoreDict)