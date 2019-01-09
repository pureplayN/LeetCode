import unittest

from leetcode.solutions._003_longest_substring_without_repeating_characters import Solution


class LongestSubstringTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testEmptyString(self):
        str = ''
        maxLength = self.solution.lengthOfLongestSubstring(str)
        self.assertEqual(maxLength, 0)

    def testSingleChar(self):
        str = 'a'
        maxLength = self.solution.lengthOfLongestSubstring(str)
        self.assertEqual(maxLength, 1)

    def testTwoChars(self):
        str = 'ab'
        maxLength = self.solution.lengthOfLongestSubstring(str)
        self.assertEqual(maxLength, 2)

    def testRepeatingChars(self):
        str = 'aaaaaaaaaaaaaaaaaa'
        maxLength = self.solution.lengthOfLongestSubstring(str)
        self.assertEqual(maxLength, 1)

    def testCommonCase(self):
        str = 'pwwkew'
        maxLength = self.solution.lengthOfLongestSubstring(str)
        self.assertEqual(maxLength, 3)

        str = 'abcabcbb'
        maxLength = self.solution.lengthOfLongestSubstring(str)
        self.assertEqual(maxLength, 3)

        str = 'abcdefaghijklmn'
        maxLength = self.solution.lengthOfLongestSubstring(str)
        self.assertEqual(maxLength, 14)

        str = 'abba'
        maxLength = self.solution.lengthOfLongestSubstring(str)
        self.assertEqual(maxLength, 2)
