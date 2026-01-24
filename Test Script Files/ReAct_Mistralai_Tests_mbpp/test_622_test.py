import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertEqual(get_median([], [], 0), None)

    def test_single_element_arrays(self):
        self.assertEqual(get_median([1], [], 1), 1)
        self.assertEqual(get_median([], [1], 1), 1)
        self.assertEqual(get_median([1], [1], 1), 1)

    def test_equal_arrays(self):
        self.assertEqual(get_median([1, 2, 3], [1, 2, 3], 3), 2)

    def test_unequal_arrays(self):
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 3), 3)

    def test_odd_length_arrays(self):
        self.assertEqual(get_median([1, 2, 3], [4, 5], 2), 2.5)
        self.assertEqual(get_median([1, 2, 3], [4], 1), 2.5)
        self.assertEqual(get_median([4], [1, 2, 3], 1), 2.5)

    def test_even_length_arrays(self):
        self.assertEqual(get_median([1, 2, 3], [4, 5], 2), (2 + 3) / 2)
        self.assertEqual(get_median([1, 2, 3], [4, 5], 3), (2 + 3) / 2)
        self.assertEqual(get_median([1, 2, 3], [4, 5], 4), (2 + 3) / 2)

    def test_arrays_with_duplicates(self):
        self.assertEqual(get_median([1, 1, 2, 3], [4, 4, 5], 3), 2)
        self.assertEqual(get_median([1, 1, 2, 3], [4, 4, 5], 4), 2)

    def test_arrays_with_negative_numbers(self):
        self.assertEqual(get_median([-1, 0, 1], [-2, 0, 2], 2), 0)
        self.assertEqual(get_median([-1, 0, 1], [-2, 0, 2], 3), 0)
