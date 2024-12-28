import math

with open("datasets/day5a.txt", "r") as file:
    rules = file.read().split('\n')

with open("datasets/day5b.txt", "r") as file:
    pages = file.read().split('\n')

precedentsDict = {}
for rule in rules:
    ruleSet = rule.split('|')
    if(ruleSet[1] in precedentsDict):
        precedentsDict[ruleSet[1]].append(ruleSet[0])
    else:
        precedentsDict.update({str(ruleSet[1]): [ruleSet[0]]})

def checkNumberValidity(index, numberList):
    number = numberList[index]
    if str(number) not in precedentsDict: #the number needs no precedent
        return True
    else: #the number needs a precedent
        requiredPrecedents = precedentsDict[str(number)]
        for requiredPrecedent in requiredPrecedents: #check that all prerequisites are met
            if(requiredPrecedent not in numberList[:index]): #the prerequisites isn't met
                if(requiredPrecedent in numberList[index:]):
                    return False
        return True

def checkNumberList(numberList):
    if(numberList == []): return False
    for index in range(0, len(numberList)):
        if not checkNumberValidity(index, numberList): return False
    return True

def checkPage(page):
    numbers = page.split(',')
    bool = checkNumberList(numbers)
    return bool

def getMiddle(list):
    numbers = list.split(',')
    return int(numbers[math.floor(len(numbers)/2)])

validPages = []
total = 0
for page in pages:
    validPage = checkPage(page)
    if(validPage):
        validPages.append(page)
        total += getMiddle(page)

print(total)
