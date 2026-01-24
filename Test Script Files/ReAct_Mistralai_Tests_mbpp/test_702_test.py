import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(removals([], 0, 0), 0)

    def test_single_element_array(self):
        for k in range(-10, 10):
            self.assertEqual(removals([1], 1, k), 0 if k == 1 else 1)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        for k in range(-10, 6):
            self.assertEqual(removals(arr, len(arr), k),
                             len(arr) - (arr.index(k) + 1) if k in arr else 0)

    def test_unsorted_array(self):
        arr = [5, 3, 4, 1, 2]
        for k in range(1, 6):
            self.assertEqual(removals(arr, len(arr), k),
                             len(arr) - (arr.index(k) + 1))

    def test_negative_k(self):
        self.assertEqual(removals([1, 2, 3], 3, -1), 2)

    def test_k_greater_than_max_array_value(self):
        self.assertEqual(removals([1, 2, 3], 3, 4), 3)

    def test_k_less_than_min_array_value(self):
        self.assertEqual(removals([1, 2, 3], 3, -2), 0)
