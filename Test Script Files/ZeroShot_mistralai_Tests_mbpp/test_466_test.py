import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_find_peak_empty_list(self):
        self.assertIsNone(find_peak([]))

    def test_find_peak_single_element(self):
        self.assertEqual(find_peak([1]), 0)

    def test_find_peak_two_elements(self):
        self.assertEqual(find_peak([1, 2]), 1)

    def test_find_peak_multiple_elements(self):
        self.assertEqual(find_peak([1, 2, 3, 2, 1]), 3)

    def test_find_peak_decreasing_elements(self):
        self.assertEqual(find_peak([3, 2, 1]), 0)

    def test_find_peak_increasing_elements(self):
        self.assertEqual(find_peak([1, 2, 3]), 2)

    def test_find_peak_multiple_peaks(self):
        self.assertEqual(find_peak([1, 2, 3, 2, 1, 2, 3]), 3)

    def test_find_peak_negative_elements(self):
        self.assertEqual(find_peak([-1, -2, -3]), 0)
