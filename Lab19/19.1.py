nums = []
with open('nums.txt') as file:
    for line in file:
        num = float(line)
        if num > 0:
            nums.append(num)
print(min(nums))