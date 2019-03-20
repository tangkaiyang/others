# def fourSum(nums, target):
#     i = 0
#     res = []
#     nums.sort()
#     while i < len(nums):
#         p = i + 1
#         q = p + 1
#         k = len(nums) - 1
#         quadriSum = nums[i] + nums[p] + nums[q] + nums[k]
#
#         while k > q:
#             if quadriSum == target:
#                 res.append([nums[i], nums[p], nums[q], nums[k]])
#                 k -= 1
#                 p += 1
#             elif quadriSum > target:
#                 k -= 1
#                 while k > q and nums[k] == nums[k + 1]:
#                     k -= 1
#             else:
#                 p += 1
#         i += 1
#
#     return list(set(res))
#
#
# print(fourSum([1, 0, -1, 0, 1], 0))
"""
018 4Sum
https://leetcode.com/problems/4Sum/
Given an array nums of n integers, are there elements a,
b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
Note: The solution set must not contain duplicate quadruplets.

Recursively reduce to 2sum problem
Time - O(n^3), for each pair perform linear search on the rest of the array
"""


def n_sum(nums, target, partial, n, results):  # generalise for n-sum
    if len(nums) < n or target > nums[-1] * n or target < nums[0] * n:  # early return if possible
        return
    if n == 2:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                results.append(partial + [nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[right] == nums[right + 1] and right > left:  # move to next different number if target found
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    else:
        for i in range(len(nums) - n + 1):  # for all possible first numbers nums[i]
            if i == 0 or nums[i] != nums[i - 1]:  # if not duplicate
                n_sum(nums[i + 1:], target - nums[i], partial + [nums[i], n - 1, results])


ELEMENTS = 4


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target : int
    :rtype: List[List[int]]
    """
    results = []
    n_sum(sorted(nums), target, [], ELEMENTS, results)
    return results


print(fourSum([1, 0, -1, 0, 1], 0))
