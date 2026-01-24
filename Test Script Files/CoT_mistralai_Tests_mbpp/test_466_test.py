import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_peak([]), None)

    def test_single_element(self):
        self.assertEqual(find_peak([1]), 0)

    def test_single_peak_at_beginning(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5]), 0)

    def test_single_peak_at_end(self):
        self.assertEqual(find_peak([5, 4, 3, 2, 1]), 4)

    def test_multiple_peaks(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 4, 5]), 3)

    def test_peak_at_boundary(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 4, 4, 5]), 5)

    def test_decreasing_sequence(self):
        self.assertEqual(find_peak([5, 4, 3, 2, 1]), None)

    def test_increasing_sequence(self):
        self.assertEqual(find_peak([1, 2, 3, 4]), None)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_peak, 'not a list')
