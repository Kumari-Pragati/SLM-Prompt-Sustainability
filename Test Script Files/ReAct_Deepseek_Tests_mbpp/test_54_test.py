import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element(self):
        self.assertEqual(counting_sort([5]), [5])

    def test_negative_numbers(self):
        self.assertEqual(counting_sort([-1, -2, -3, -2, -1]), [-3, -2, -2, -1, -1])

    def test_large_numbers(self):
        self.assertEqual(counting_sort([100, 200, 300, 200, 100]), [100, 100, 200, 200, 300])

    def test_duplicate_elements(self):
        self.assertEqual(counting_sort([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_mixed_numbers(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_large_range(self):
        self.assertEqual(counting_sort(list(range(1, 10001))), list(range(1, 10001)))
