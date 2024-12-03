f = open("datasets/day2.txt", "r")
lines = f.readlines()

safe_reports = 0
def safeLine(line, increasing):
    if(len(line) < 2): #stop condition
        return 1 #1 means success
    if(
        (increasing is not None and (increasing != (line[0] < line[1]))) #directin change
        or (abs(line[0] - line[1]) > 3) #too steep increment
        or (line[0] == line[1]) #no change
        ):
            return 0
    return safeLine(line[1:], line[0] < line[1]) #recurse

def checkFaultyLines(line):
    print("initial", line)
    for index, item in enumerate(line):
        sliceLine = line[:index] + line[index+1:]
        print(sliceLine)
        result = safeLine(sliceLine, None)
        print(result, index)
        if(result == 1):
            return 1
    return 0

for line in lines:
    line = line.replace("\n", "").split(' ')
    line = list(map(int, line))
    result = safeLine(line, None)
    safe_reports += result
    if(result < 1):
        safe_reports += checkFaultyLines(line)

print("safe_reports", safe_reports)