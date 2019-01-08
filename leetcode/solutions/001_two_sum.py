class Solution:
    def twoSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        copy = nums.copy()
        nums.append(int(target / 2))
        targetIndex = self.quickSortAndFindTargetHalfIndex(nums)
        if targetIndex == 0:
            small = copy.index(nums[target])
            great = copy.index(nums[target], small)
            return (small, great)
        for great in range(len(nums) - 1, targetIndex, -1):
            for small in range(0, targetIndex):
                if nums[great] + nums[small] > target:
                    break
                elif nums[great] + nums[small] < target:
                    continue
                else:
                    return (copy.index(nums[small]), copy.index(nums[great]))

    def quickSortAndFindTargetHalfIndex(self, nums):
        targetIndex = self.partition(nums, 0, len(nums) - 1)
        self.quick_sort_impl(nums, 0, targetIndex - 1)
        self.quick_sort_impl(nums, targetIndex + 1, len(nums) - 1)
        return targetIndex

    def quick_sort_impl(self, nums, front, end):
        if front < end:
            mid = self.partition(nums, front, end)
            self.quick_sort_impl(nums, front, mid - 1)
            self.quick_sort_impl(nums, mid + 1, end)

    def partition(self, nums, front, end):
        mid_item = nums[end]
        lt_end = front - 1
        for i in range(front, end):
            if nums[i] <= mid_item:
                lt_end += 1
                if lt_end != i:
                    nums[i], nums[lt_end] = nums[lt_end], nums[i]
        nums[lt_end + 1], nums[end] = nums[end], nums[lt_end + 1]
        return lt_end + 1