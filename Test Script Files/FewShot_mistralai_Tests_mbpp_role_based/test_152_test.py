import unittest
from mbpp_152_code import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_mixed_list(self):
        self.assertEqual(merge_sort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_long_list(self):
        long_list = [i for i in range(100)]
        random.shuffle(long_list)
        self.assertEqual(merge_sort(long_list), sorted(long_list))

    def test_list_with_duplicates(self):
        self.assertEqual(merge_sort([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])
