import unittest

from leetcode.solutions._007_reverse_interger import Solution


class ReverseInterger(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testOneBitPositive(self):
        x = 8
        r = self.solution.reverse(x)
        self.assertEqual(x, r)

    def testMultiBitsPositive(self):
        x = 12345
        r = self.solution.reverse(x)
        self.assertEqual(r, 54321)

    def testPositiveEndWith0s(self):
        x = 120000
        r = self.solution.reverse(x)
        self.assertEqual(r, 21)

    def testOneBitNegtive(self):
        x = -9
        r = self.solution.reverse(x)
        self.assertEqual(x, r)

    def testMultiBitsNegtive(self):
        x = -123478
        r = self.solution.reverse(x)
        self.assertEqual(r, -874321)

    def testNegtiveEndWith0s(self):
        x = -3400000
        r = self.solution.reverse(x)
        self.assertEqual(r, -43)
