from unittest import TestCase

from leetcode.sorting import insertion_sort, quick_sort


class TestSortBase(TestCase):

    def __init__(self, sorter):
        self._sorter = sorter

    def test_sort_None_properly(self):
        try:
            self._sorter(None)
        except:
            self.fail('test_sort_None_properly() failed with exception raised!')

    def test_sort_Empty_properly(self):
        try:
            self._sorter([])
        except:
            self.fail('test_sort_Empty_property() failed with exception raised!')

    def test_sort_one_item_rightly(self):
        try:
            self._sorter([1])
        except:
            self.fail('test_sort_one_item_rightly() failed with exception raised!')

    def test_sort_two_items_rightly(self):
        try:
            self._sorter([9,1])
        except:
            self.fail('test_sort_two_items_rightly() failed with exception raised!')


class TestInsertionSort(TestSortBase):
    def __init__(self):
        super.__init__(insertion_sort)


class TestQuickSort(TestSortBase):
    def __init__(self):
        super.__init__(quick_sort)
