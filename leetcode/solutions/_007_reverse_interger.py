class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            result = -self.__reversePositiveInterger(abs(x))
            if result < - pow(2, 31):
                return 0
            return result
        else:
            result = self.__reversePositiveInterger(x)
            if result > pow(2, 31) - 1:
                return 0
            return  result

    def __reversePositiveInterger(self, x):
        """
        :param x: int
        :return: int
        """
        stack = []
        num = x
        while num > 0:
            div, mod = divmod(num, 10)
            stack.append(mod)
            num = div
        result = 0
        times = 1
        while len(stack) > 0:
            i = stack.pop()
            result += i * times
            times = times * 10
        return result
