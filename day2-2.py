f = open("datasets/day2.txt", "r")
lines = f.readlines()

safe_reports = 0
def safeLine(line, increasing):
    # print(line, increasing)
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
    # if(result < 1):
    #     safe_reports += checkFaultyLines(line)

print("safe_reports", safe_reports)
    

    # if(recurse_result[0] == 1 or recurse_result[0] == 0):
    #     return recurse_result
    # #This part should only run at index 0
    # if(index == 0 and recurse_result[0] < 0):
    #     # print("index", index, type(index))
    #     print("recurse", recurse_result)
    #     # del line[recurse_result[1]] #remove first falty index

    #     if(try1[0] == 1):
    #         return (1, index)
    #     print("try2",try2)
    #     if(try2[0] == 1):
    #         return (1, index)
    #     return (0, index)