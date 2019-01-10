class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        cycle = numRows + numRows - 2
        rows = []
        for i in range(0, numRows):
            rows.append([])
        cylIndex = 0
        for i in range(0, len(s)):
            if cylIndex < numRows:
                targetRowIndex = cylIndex
            else:
                targetRowIndex = numRows - (cylIndex + 1 - numRows) - 1
            rows[targetRowIndex].append(s[i])
            cylIndex += 1
            if cylIndex >= cycle:
                cylIndex = 0
        result = ''
        for row in rows:
            result += ''.join(row)
        return result




