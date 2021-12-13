with open('input2.txt') as file:
    nums = [int(i) for i in file.readlines()]


print(nums)
l = len(nums)
for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
