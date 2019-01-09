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
        lHead = ListNode(0)
        lResultBit = lHead
        carry = 0
        while l1 or l2 or carry > 0:
            value, carry = self.__addBit(l1, l2, carry)
            lResultBit.next = ListNode(value)
            lResultBit = lResultBit.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
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
    def setUp(self):
        self.solution = Solution()

    def testAddTwoZeroNumber(self):
        l1 = self.__buildLinkedList([0])
        l2 = self.__buildLinkedList([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertAsSupposed(result, [0])

    def testAddTwoSameLengthNumbersWithCarry(self):
        l1 = self.__buildLinkedList([9])
        l2 = self.__buildLinkedList([9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertAsSupposed(result, [8, 1])

    def testAddTwoDifferentLengthNumbersNoCarry(self):
        l1 = self.__buildLinkedList([3])
        l1.val = 3
        l2 = self.__buildLinkedList([3, 3, 3])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertAsSupposed(result, [6, 3, 3])

    def testAddTwoDifferentLengthNumbersWithCarry(self):
        l1 = self.__buildLinkedList([8, 8, 8])
        l2 = self.__buildLinkedList([8, 9, 8, 5])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertAsSupposed(result, [6, 8, 7, 6])

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
        lHead = ListNode(0)
        lNode = lHead
        for i in seq:
            lNode.next = ListNode(i)
            lNode = lNode.next
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
