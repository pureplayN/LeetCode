import unittest

from leetcode.solutions._008_atoi import Solution


class AtoiTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testStartNotWithNumericalItems(self):
        s ="words and 987"
        r = self.solution.myAtoi(s)
        self.assertEqual(0, r)

    def testStartWithPlus(self):
        s = '+893'
        r = self.solution.myAtoi(s)
        self.assertEqual(893, r)

    def testStartWithMinus(self):
        s = '-839'
        r = self.solution.myAtoi(s)
        self.assertEqual(r, -839)

    def testStartWithEmpty(self):
        s = '      422 usnda'
        r = self.solution.myAtoi(s)
        self.assertEqual(r, 422)

    def testOverLimit(self):
        s = "-91283472332"
        r = self.solution.myAtoi(s)
        self.assertEqual(-2147483648, r)

        s = "91283472331"
        r = self.solution.myAtoi(s)
        self.assertEqual(2147483647, r)

    def testPlusMinusTogether(self):
        s = '+-2'
        r = self.solution.myAtoi(s)
        self.assertEqual(0, r)

    def testBlankBetweenOpAndNum(self):
        s = '- 2'
        r = self.solution.myAtoi(s)
        self.assertEqual(0, r)
