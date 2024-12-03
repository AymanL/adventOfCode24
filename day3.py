import re 

with open("datasets/day3.txt", "r") as file:
    data = file.read().replace('\n', '')

def mul_match(line):
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
    return result

total = 0
left_data = data
groups = [x.group() for x in re.finditer(r'.+?(?=(do\(\)|don\'t\(\)))', data)]

for group in groups:
    left_data = left_data[len(group):]
    result = mul_advanced_match(group)
    print(group, result)
    total += result
total += mul_match(left_data)
print(total)
print(left_data)