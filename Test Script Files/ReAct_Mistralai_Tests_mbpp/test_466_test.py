import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_peak([], 0), None)

    def test_single_element_list(self):
        self.assertEqual(find_peak([1], 1), 0)

    def test_single_peak_in_middle(self):
        self.assertEqual(find_peak([1, 2, 3, 2, 1], 5), 3)

    def test_single_peak_at_beginning(self):
        self.assertEqual(find_peak([3, 2, 1], 3), 0)

    def test_single_peak_at_end(self):
        self.assertEqual(find_peak([1, 2, 3], 3), 2)

    def test_multiple_peaks_in_middle(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 3, 2, 1], 8), 4)

    def test_peak_and_valley_in_middle(self):
        self.assertEqual(find_peak([1, 2, 3, 2, 1, 0], 6), 4)

    def test_decreasing_sequence(self):
        self.assertEqual(find_peak([3, 2, 1], 3), None)

    def test_increasing_sequence(self):
        self.assertEqual(find_peak([1, 2, 3], 3), None)

    def test_negative_numbers(self):
        self.assertEqual(find_peak([-1, -2, -3], 3), None)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(find_peak([-1, 1, 2, 3], 4), None)
