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
        if p[0] == '*':
            raise Exception('Invalid pattern:' + p)

        match, headMatchCount, tearMatchCount = self.__isFixedSliceMatch(s, p)
        if not match:
            return False
        if match and headMatchCount == len(p):
            return True

        unfixedS = s[headMatchCount:len(s) - tearMatchCount]
        unfixedP = p[headMatchCount:len(p) - tearMatchCount]
        if len(unfixedP) == 2:
            if unfixedP[0] == '.':
                return True
            elif unfixedP[0] == '*':
                raise Exception('Invalid pattern:' + p)
            else:
                for c in unfixedS:
                    if c != unfixedP[0]:
                        return False
                return True
        elif len(unfixedP) == 3:
            raise Exception('Invalid pattern:' + p)
        else:
            subP = unfixedP[2:]
            thisUnfixed = unfixedP[0:2]
            matchSub = False
            shifting = 0
            while shifting <= len(unfixedS) and (not matchSub) and self.isMatch(unfixedS[0:shifting], thisUnfixed):
                matchSub = self.isMatch(unfixedS[shifting:], subP)
                shifting += 1
            return matchSub

    def __isFixedSliceMatch(self, s, p):
        complete = True
        headMatchCount, tearMatchCount = 0, 0
        for i in range(0, len(p)):
            if i + 1 < len(p) and p[i+1] == '*':
                complete = False
                break
            elif i >= len(s):
                return False, -1, -1
            elif p[i] == s[i] or p[i] == '.':
                headMatchCount += 1
            else:
                return False, -1, -1

        if not complete:
            s = s[headMatchCount:]
            for i in range(1, len(p)):
                pIndex = len(p) - i
                sIndex = len(s) - i
                if p[pIndex] == '*':
                    break
                elif sIndex < 0:
                    return False, -1, -1
                elif p[pIndex] == s[sIndex] or p[pIndex] == '.':
                    tearMatchCount += 1
                else:
                    return False, -1, -1
        elif len(s) > headMatchCount:
            return False, -1, -1

        return True, headMatchCount, tearMatchCount



