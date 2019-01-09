"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            nums1 = []
        if not nums2:
            nums2 = []

        participantsOrders = self.__getMedianPaticipantsOrders(nums1, nums2)
        if len(nums1) == 0:
            return self.__getMedianFromSingleArray(nums2, participantsOrders)
        elif len(nums2) == 0:
            return self.__getMedianFromSingleArray(nums1, participantsOrders)
        if nums1[len(nums1) - 1] < nums2[0]:
            return self.__getMedianFromNoIntersectionArrays(nums1, nums2, participantsOrders)
        elif nums1[0] > nums2[len(nums2) - 1]:
            return self.__getMedianFromNoIntersectionArrays(nums2, nums1, participantsOrders)
        else:
            return self.__getMedianFromWithIntersectionArrays(nums1, nums2, participantsOrders)

    @staticmethod
    def __getMedianFromWithIntersectionArrays(nums1, nums2, orders):
        findOrderIndex = 0
        nums1Index = 0
        nums2Index = 0
        currentOrder = 1
        total = 0
        while findOrderIndex < len(orders):
            if nums1Index >= len(nums1):
                currentOrderValue = nums2[nums2Index]
                nums2Index += 1
            elif nums2Index >= len(nums2):
                currentOrderValue = nums1[nums1Index]
                nums1Index += 1
            elif nums1[nums1Index] < nums2[nums2Index]:
                currentOrderValue = nums1[nums1Index]
                nums1Index += 1
            else:
                currentOrderValue = nums2[nums2Index]
                nums2Index += 1
            if currentOrder == orders[findOrderIndex]:
                total += currentOrderValue
                findOrderIndex += 1
            currentOrder += 1
        return total / len(orders)



    @staticmethod
    def __getMedianFromNoIntersectionArrays(smallers, greaters, orders):
        total = 0
        for order in orders:
            if order > len(smallers):
                total += greaters[order - len(smallers) - 1]
            else:
                total += smallers[order - 1]
        return total / len(orders)

    @staticmethod
    def __getMedianFromSingleArray(nums, orders):
        total = 0
        for order in orders:
            total += nums[order - 1]
        return total / len(orders)

    @staticmethod
    def __getMedianPaticipantsOrders(nums1, nums2):
        total = len(nums1) + len(nums2)
        order1 = total // 2
        if total % 2 > 0:
            return [order1 + 1]
        else:
            return [order1, order1 + 1]

