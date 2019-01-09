# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lHead = ListNode()
        lResultBit = lHead
        carry = 0
        while l1 or l2 or carry > 0:
            lResultBit.next = ListNode()
            lResultBit = lResultBit.next
            value, carry = self.__addBit(l1, l2, carry)
            lResultBit.val = value
        return lHead.next

    def __addBit(self, l1, l2, carry):
        bitValue = carry
        if l1:
            bitValue += l1.val
        if l2:
            bitValue += l2.val
        carry = bitValue // 10
        return (bitValue - 10 * carry, carry)


import unittest


class SolutionTest(unittest.TestCase):
    def __init__(self):
        super.__init__()
        self.solution = Solution()

    def testAddTwoZeroNumber(self):
        l1 = self.__buildLinkedList([0])
        l2 = self.__buildLinkedList([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertTrue(self.assertAsSupposed(result, [0]))

    def testAddTwoSameLengthNumbersWithCarry(self):
        l1 = self.__buildLinkedList([9])
        l2 = self.__buildLinkedList([9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertTrue(self.assertAsSupposed(result, [8, 1]))

    def testAddTwoDifferentLengthNumbersNoCarry(self):
        l1 = ListNode()
        l1.val = 3
        l2 = ListNode()
        l2.val = 7
        l2.next = ListNode()
        l2.next

    def assertAsSupposed(self, lResult, supposeSeq):
        if not lResult:
            raise Exception('Supposed:' + self.__getPrintText(supposeSeq)
                    + ', get: None')
        lNode = lResult
        for i in supposeSeq:
            if not lNode or lNode.val != i:
                raise Exception('Supposed:' + self.__getPrintText(supposeSeq)
                        + ', get:' + self.__getPrintText(lResult))
            else:
                lNode = lNode.next

    def __buildLinkedList(self, seq):
        lHead = ListNode()
        lNode = lHead
        lNode.val = seq[0]
        for i in seq:
            lNode.next = ListNode()
            lNode = lNode.next
            lNode.val = i
        return lHead.next


    def __getPrintText(self, seq):
        text = None
        if isinstance(seq, list):
            text += str(seq[0])
            for i in range(1, len(seq)):
                text += '-->' + str(seq[i])
        elif isinstance(seq, ListNode):
            text += str(seq.val)
            while seq.next:
                text += '-->' + str(seq.next.val)
                seq = seq.next
        else:
            raise TypeError('cannot get print text for type:' + type(seq))
