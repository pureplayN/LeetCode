import unittest

from leetcode.solutions._005_longest_palindrome import Solution


class LongestPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testSamples(self):
        samples = {
            '': [''],
            'babad': ['bab', 'aba'],
            'cbbd': ['bb'],
            'aaaaaaaa': ['aaaaaaaa'],
            'acbaaabcvkycb': ['cbaaabc']
        }
        for (s, r) in samples.items():
            result = self.solution.longestPalindrome(s)
            self.assertIn(result, r)

