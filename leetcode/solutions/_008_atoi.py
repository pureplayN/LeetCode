class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        negtive = False
        startIndex = -1
        pmOccurs = 0
        for i in range(0, len(str)):
            if str[i] == '+':
                negtive = False
                pmOccurs += 1
            elif str[i] == '-':
                negtive = True
                pmOccurs += 1
            elif '0' <= str[i] <= '9':
                startIndex = i
                break
            elif str[i] == ' ':
                if pmOccurs > 0:
                    break
                else:
                    continue
            else:
                break
            if pmOccurs > 1:
                break

        if startIndex < 0:
            return 0

        stack = []
        for i in range(startIndex, len(str)):
            if '0' <= str[i] <= '9':
                stack.append(ord(str[i]) - 48)
            else:
                break

        result = 0
        times = 1
        while len(stack) > 0:
            ele = stack.pop()
            result += ele * times
            times *= 10
            if result > 2147483647:
                result = 2147483648 if negtive else 2147483647
                break

        if result > 0 and negtive:
            return -result
        else:
            return result



