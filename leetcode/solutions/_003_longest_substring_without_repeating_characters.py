class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        longest = [0, 0]
        current = [0, 0]
        dict = { s[0]: 0 }
        for i in range(1, len(s)):
            if s[i] in dict.keys():
                # set current to longest if longger
                if current[1] - current[0] > longest[1] - longest[0]:
                    longest[0] = current[0]
                    longest[1] = current[1]
                # maitain current and dict
                for j in range(current[0], dict[s[i]]):
                    dict.pop(s[j], None)
                current[0] = dict[s[i]] + 1
                current[1] = i
                dict[s[i]] = i
            else:
                # add this char to current
                current[1] = i
                dict[s[i]] = i
        if current[1] - current[0] > longest[1] - longest[0]:
            longest = current
        return longest[1] - longest[0] + 1
