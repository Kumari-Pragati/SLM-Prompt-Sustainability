import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(raw_heap([3, 5, 1, 7, 2]), [1, 2, 3, 5, 7])

    def test_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element(self):
        self.assertEqual(raw_heap([4]), [4])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-3, -5, -1, -7, -2]), [-3, -2, -5, -7, -1])

    def test_duplicates(self):
        self.assertEqual(raw_heap([3, 3, 1, 7, 2]), [1, 2, 3, 3, 7])

    def test_sorted_list(self):
        self.assertEqual(raw_heap([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reversed_list(self):
        self.assertEqual(raw_heap([7, 6, 5, 4, 3]), [3, 4, 5, 6, 7])

    def test_large_list(self):
        large_list = [i for i in range(100)]
        self.assertEqual(raw_heap(large_list), sorted(large_list))
