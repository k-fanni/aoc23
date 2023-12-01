import re

input = []
nums = []
with open('challenge01_input.txt', 'r') as f:
    for row in f:
        r = re.sub(r"\D", "", row.strip())
        input.append(r)

for rawNum in input:
    if len(rawNum) == 1:
        nums.append(int(rawNum * 2))
    elif len(rawNum) > 2:
        nums.append(int(rawNum[0] + rawNum[-1]))
    else:
        nums.append(int(rawNum))
    
print(nums)

# result
print(sum(nums))