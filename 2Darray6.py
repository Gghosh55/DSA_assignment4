def sorted_squares(nums):
    squared_nums = []
    for num in nums:
        squared_nums.append(num * num)
    squared_nums.sort()
    return squared_nums
nums = [-4, -1, 0, 3, 10]
print(sorted_squares(nums))
