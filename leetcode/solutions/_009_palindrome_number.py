class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            div, mod = divmod(x, 10)
            bits = [mod]
            while div > 0:
                div, mod = divmod(div, 10)
                bits.append(mod)
            start, stop = 0, len(bits) - 1
            while start < stop:
                if bits[start] != bits[stop]:
                    return False
                start += 1
                stop -= 1
            return True
