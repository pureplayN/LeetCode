class Solution:
    def twoSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        dict = {}
        for i in range(0, len(nums)):
            completion = target - nums[i]
            if completion in dict.keys():
                return (dict[completion], i)
            else:
                dict[nums[i]] = i
