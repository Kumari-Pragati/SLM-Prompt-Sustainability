import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_get_median_with_equal_length_arrays(self):
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)

    def test_get_median_with_first_array_longer(self):
        self.assertAlmostEqual(get_median([1, 3, 5, 7], [2, 4, 6], 3), 4.0)

    def test_get_median_with_second_array_longer(self):
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6, 8], 3), 4.0)

    def test_get_median_with_single_element_arrays(self):
        self.assertAlmostEqual(get_median([1], [2], 1), 1.5)

    def test_get_median_with_same_elements(self):
        self.assertAlmostEqual(get_median([1, 2, 3], [1, 2, 3], 3), 2.0)

    def test_get_median_with_empty_arrays(self):
        self.assertRaises(ValueError, get_median, [], [], 0)
