import re 

with open("datasets/day3.txt", "r") as file:
    data = file.read().replace('\n', '')

def mul_match(line):
    print("line2", line)
    mul_matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
    total = 0
    for mul in mul_matches:
        numbers = list(map(int, mul[4:-1].split(',')))
        total += numbers[0] * numbers[1]
    return total

def mul_advanced_match(line):
    use = line[:7] != "don't()"
    if(not use):
        return 0
    result = mul_match(line)
    print("result", result)
    return result

mul_matches = re.findall(r'.+?(?=(do\(\)|don\'t\(\)))', data)
total = 0

groups = [x.group() for x in re.finditer(r'.+?(?=(do\(\)|don\'t\(\)))', data)]
i = 1
for group in groups:
    # print(group)
    total += mul_advanced_match(group)
    i += 1
    if(i==5):
        break
    
print(total)
# print(168*87 + 911*800+ 734*19+ 829*495)
# print(168*87)
# mul(168,87)}*:mul(911,800)(%,)where()#&&$mul(734,19)?when()why(){$:?mul(829,495)