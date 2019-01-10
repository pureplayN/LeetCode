class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or s == '':
            return ''
        longest = [0, 0]
        for i in range(0, len(s) - 1):
            asCenterLongest = self.__findLongestPalindromeWithMemberAsCenter(i, s)
            if asCenterLongest and asCenterLongest[1] - asCenterLongest[0] > longest[1] - longest[0]:
                longest[0], longest[1] = asCenterLongest[0], asCenterLongest[1]
            withNextLongest = self.__findLongestPalindromeWithMemberAndNextAsCenter(i, s)
            if withNextLongest and withNextLongest[1] - withNextLongest[0] > longest[1] - longest[0]:
                longest[0], longest[1] = withNextLongest[0], withNextLongest[1]
        return s[longest[0]:longest[1] + 1]

    @staticmethod
    def __findLongestPalindromeWithMemberAsCenter(memberIndex, s):
        expandWidth = 1
        while memberIndex - expandWidth >= 0 and memberIndex + expandWidth < len(s)\
            and s[memberIndex - expandWidth] == s[memberIndex + expandWidth]:
            expandWidth += 1
        expandWidth -= 1
        if expandWidth > 0:
            return [memberIndex - expandWidth, memberIndex + expandWidth]
        else:
            return None

    @staticmethod
    def __findLongestPalindromeWithMemberAndNextAsCenter(memberIndex, s):
        if memberIndex + 1 >= len(s) or s[memberIndex] != s[memberIndex + 1]:
            return None
        expandWitdh = 1
        while memberIndex - expandWitdh >= 0 and memberIndex + expandWitdh + 1 < len(s)\
            and s[memberIndex - expandWitdh] == s[memberIndex + expandWitdh + 1]:
            expandWitdh += 1
        expandWitdh -= 1
        return [memberIndex - expandWitdh, memberIndex + expandWitdh + 1]
