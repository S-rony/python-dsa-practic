nums = [3, 3, 6, 1]
max = 0
for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]
print(max)
