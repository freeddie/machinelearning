'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Max_indicator = len(nums)-1
        for i in range(Max_indicator):
            for j in range(i+1,Max_indicator+1):
                if nums[i]+nums[j] == target:
                    return [i,j]


            