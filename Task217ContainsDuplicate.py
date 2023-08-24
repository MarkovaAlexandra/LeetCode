# Given an integer array nums,return true if any value appears
# at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    for i in range (0, len(nums) - 1):
        if (nums[i] == nums[i + 1]):
            return True
            break
    return False


