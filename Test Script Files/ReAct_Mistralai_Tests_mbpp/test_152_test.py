import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        for num in range(10):
            self.assertEqual(merge_sort([num]), [num])

    def test_sorted_list(self):
        test_list = [5, 3, 8, 1, 6, 9, 2, 7, 4]
        sorted_list = sorted(test_list)
        self.assertEqual(merge_sort(test_list), sorted_list)

    def test_reverse_sorted_list(self):
        test_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_list = sorted(test_list, reverse=True)
        self.assertEqual(merge_sort(test_list), sorted_list)

    def test_mixed_list(self):
        test_list = [5, 3, 8, 1, 6, 9, 2, 7, 4, 10, 20, 1]
        sorted_list = sorted(test_list)
        self.assertEqual(merge_sort(test_list), sorted_list)

    def test_large_list(self):
        test_list = [random.randint(0, 100) for _ in range(1000)]
        sorted_list = sorted(test_list)
        self.assertEqual(merge_sort(test_list), sorted_list)
