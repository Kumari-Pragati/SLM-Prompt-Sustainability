import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_negative_numbers(self):
        self.assertEqual(counting_sort([-2, -5, -3, -6, -1]), [-6, -5, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(counting_sort([3, -1, 2, -5, 1, 4]), [-5, -1, 1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element(self):
        self.assertEqual(counting_sort([5]), [5])
