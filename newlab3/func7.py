def has_adjacent_threes(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Example usage:
result1 = has_adjacent_threes([1, 2, 3, 3, 4])  # True
result2 = has_adjacent_threes([1, 2, 3, 4, 5])  # False
result3 = has_adjacent_threes([3, 3, 5, 6])  # True

print(result1)
print(result2)
print(result3)