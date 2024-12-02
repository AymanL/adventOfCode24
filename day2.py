f = open("datasets/day2.txt", "r")
lines = f.readlines()

safe_reports = 0
def safeLine(line, increasing):
    if(len(line) < 2): # stop condition
        return 1
    if(
        (increasing is not None and (increasing != (line[0] < line[1]))) #directin change
        or (abs(line[0] - line[1]) > 3) #too steep increment
        or (line[0] == line[1]) #no change
        ):
            return 0
    return safeLine(line[1:], line[0] < line[1]) #recurse

for line in lines:
    line = line.replace("\n", "").split(' ')
    line = list(map(int, line))
    safe_reports += safeLine(line, None)

print(safe_reports)
    
