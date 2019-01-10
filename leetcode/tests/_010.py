import unittest

from leetcode.solutions._010_regular_expression_matching import Solution


class RegularExpressionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testPureStringNotMatch(self):
        s = 'aabbccdd'
        p = 'aabbcdd'
        self.assertFalse(self.solution.isMatch(s, p))

    def testPureStringMatch(self):
        s = 'a'
        p = 'a'
        self.assertTrue(self.solution.isMatch(s, p))

    def testEmptyMatch(self):
        s = ''
        p = ''
        self.assertTrue(self.solution.isMatch(s, p))

        s = ''
        p = 'a*'
        self.assertTrue(self.solution.isMatch(s, p))

        s = 'dsds'
        p = ''
        self.assertFalse(self.solution.isMatch(s, p))


    def testStartWithAnySubStringMatch(self):
        s = 'kmfkdlkdkijdskdsidskdskijdskds'
        p = '.*ijdskds'
        self.assertTrue(self.solution.isMatch(s, p))

    def testStartWithAnySubStringNotMatch(self):
        s = 'kmfkdlkdkijdskdsidskdskijdskds'
        p = '*jdskdsj'
        self.assertFalse(self.solution.isMatch(s, p))

    def testSingleCharRepeatingMatch(self):
        s = 'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
        p = 'i*iiii'
        self.assertTrue(self.solution.isMatch(s, p))

        s = 'iiii'
        p = 'i*iiii'
        self.assertTrue(self.solution.isMatch(s, p))

    def testSingleCharNotMatch(self):
        s = 'iii'
        p = 'i*iiii'
        self.assertFalse(self.solution.isMatch(s, p))
