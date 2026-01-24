import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(find_peak([1], 1), 0)

    def test_single_peak_in_middle(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 3)

    def test_single_peak_at_beginning(self):
        self.assertEqual(find_peak([5, 4, 3, 2, 1], 5), 0)

    def test_single_peak_at_end(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_multiple_peaks(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 4, 5], 6), 3)

    def test_decreasing_array(self):
        self.assertEqual(find_peak([5, 4, 3, 2, 1], 5), None)

    def test_increasing_array(self):
        self.assertEqual(find_peak([1, 2, 3], 3), None)

    def test_empty_array(self):
        self.assertEqual(find_peak([], 0), None)
