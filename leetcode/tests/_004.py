import unittest

from leetcode.solutions._004_median_of_two_sorted_array import Solution


class MedianOfTwoSortedArrayTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testOneOfNumsArraysEmpty(self):
        nums1 = [2, 4, 5, 8, 9]
        nums2 = []
        median = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(median, 5)

    def testEvenNumsArraysWithoutIntersection(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [6, 7, 9]
        median = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(median, 4)

    def testEvenTotalCountNumsArrays(self):
        nums1 = [1, 3, 6]
        nums2 = [4, 5, 9, 11]
        median = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(median, 5)

    def testOddTotalCountNumsArrays(self):
        nums1 = [1, 3, 6, 10]
        nums2 = [4, 5, 9, 11, 33, 56]
        median = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(median, (6 + 9) / 2)

