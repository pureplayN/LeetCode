import unittest

from leetcode.solutions._009_palindrome_number import Solution


class PalindromeNumberTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testNegtiveNumbers(self):
        negtives = [-2, -909, -8778]
        for i in negtives:
            self.assertFalse(self.solution.isPalindrome(i))

    def testOneBitNumber(self):
        num = 8
        r = self.solution.isPalindrome(num)
        self.assertTrue(r)

    def testTwoBitPalindromeNumber(self):
        num = 88
        r = self.solution.isPalindrome(num)
        self.assertTrue(r)

    def testTwoBitNotPalindromeNumber(self):
        num = 89
        r = self.solution.isPalindrome(num)
        self.assertFalse(r)

    def testEvenBitsPalindromeNumber(self):
        num = 97899879
        r = self.solution.isPalindrome(num)
        self.assertTrue(r)

    def testOddBitsPalindromeNumber(self):
        num = 900989009
        r = self.solution.isPalindrome(num)
        self.assertTrue(r)

    def testEvenBitsNotPalindromeNumber(self):
        num = 978399879
        r = self.solution.isPalindrome(num)
        self.assertFalse(r)

    def testOddBitsNotPalindromeNumber(self):
        num = 9009894009
        r = self.solution.isPalindrome(num)
        self.assertFalse(r)
