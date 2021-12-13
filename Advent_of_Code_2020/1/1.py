with open('input1.txt') as file:
    nums = {}

    for num in file.readlines():
        num = int(num)
        if num in nums:
            res = num*(2020-num)
        else:
            nums[2020-num] = num

print(res)
