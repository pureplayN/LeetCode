class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) > 0 and len(p) == 0:
            return False

        match, start, stop = self.__isFixedSliceMatch(p, s)
        if match and start < 0:
            return True

        unfixedS, unfixedP = s[start:stop - start + 1], p[start:stop - start + 1]
        if len(unfixedP) == 2:
            if unfixedP[0] == '.':
                return True
            elif p[0] == '*':
                raise Exception('Invalid pattern:' + p)
            else:
                for c in unfixedS:
                    if c != p[0]:
                        return False
                return True
        elif len(unfixedP) == 3:
            raise Exception('Invalid pattern:' + p)
        else:
            subP = p[2:0]
            thisUnfixed = p[0:2]
            matchSub = False
            shifting = 0
            while (not matchSub) and self.isMatch(s[0:shifting], thisUnfixed)\
                and shifting < len(s):
                matchSub = self.isMatch(s[shifting:], subP)
                shifting += 1
            return matchSub

    def __isFixedSliceMatch(self, p, s):
        if len(p) == 2 and p[1] == '*':
            return True, 0, 2
        elif len(s) == 0:
            return False, -1, -1

        complete = True
        unfixedStartIndex, unfixedStopIndex = -1, -1
        for i in range(0, len(p)):
            if i + 1 < len(p) and p[i+1] == '*':
                complete = False
                unfixedStartIndex = i
                break
            elif p[i] != s[i]:
                return False, -1, -1

        if not complete:
            for i in range(len(p) - 1, -1, -1):
                if i == '*':
                    unfixedStopIndex = i
                    break
                elif p[i] == s[i]:
                    return False, -1, -1
        return True, unfixedStartIndex, unfixedStopIndex



