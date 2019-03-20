# https://leetcode.com/problems/3sum/
# Given an array S of n integers, are there elements
# a, b, c in S such that a+b+c = 0?
# Find all unique triplets in the array which gives the sum of zero
# Note: The solution set must not contain duplicate(重复的)triplets.
# Sort the array, For each index i perform a bidirectional(双向的)
# search on the higher values in the array.
# Skip over duplicates. Increment i to the next new minimum number.
# Time - O(n**2), for each i at least one of j and k moves every iteration
# Space - O(n)
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    nums.sort()

    i = 0
    while i < len(nums):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            triple_sum = nums[i] + nums[j] + nums[k]

            if triple_sum == 0: # record result and move both j and k next new numbers
                results.append([nums[i], nums[j], nums[k]])
                k -= 1
                while k > j and nums[k] == nums[k+1]:
                    k -= 1
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
            elif triple_sum > 0: # decrement k to next new number
                k -= 1
                while k > j and nums[k] == nums[k + 1]:
                    k -= 1
            else: # increment j to next new number
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
        i += 1                  # increment i to next new number
        while i < len(nums) - 2 and nums[i] == nums[i - 1]:
            i += 1
    return results


print(threeSum([-1, -1, 0, 1, 2, 3, -5, -11, 10, 2, 4]))