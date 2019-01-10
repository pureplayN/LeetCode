import unittest

from leetcode.solutions._006_zigzag_convention import Solution


class ZigzagConventionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testEmptyStr(self):
        s = ''
        r = self.solution.convert(s, 3)
        self.assertEqual(r, '')

    def testOneRow(self):
        s = 'WEERTTYYY'
        r = self.solution.convert(s, 1)
        self.assertEqual(s, r)

    def testTwoRow(self):
        s = 'JDLWLDVB'
        r = self.solution.convert(s, 2)
        self.assertEqual(r, 'JLLVDWDB')

    def testWithinOneCycle(self):
        s = 'QWERTYJK'
        r = self.solution.convert(s, 5)
        self.assertEqual(r, 'QWKEJRYT')

    def testMoreThanOneCycle(self):
        s = 'QWERTYJKMNBVCXZ'
        r = self.solution.convert(s, 5)
        self.assertEqual(r, 'QMWKNEJBZRYVXTC')
