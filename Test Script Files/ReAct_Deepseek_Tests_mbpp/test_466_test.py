import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 20, 4, 1, 0]
        self.assertEqual(find_peak(arr, len(arr)), 2)

    def test_single_element(self):
        arr = [5]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_decreasing_sequence(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_increasing_sequence(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_peak(arr, len(arr)), 9)

    def test_peak_at_beginning(self):
        arr = [10, 4, 2, 1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_peak_at_end(self):
        arr = [1, 2, 3, 10]
        self.assertEqual(find_peak(arr, len(arr)), 3)

    def test_no_peak(self):
        arr = [1, 2, 3, 4, 5]
        self.assertIsNone(find_peak(arr, len(arr)))

    def test_empty_array(self):
        arr = []
        self.assertIsNone(find_peak(arr, len(arr)))
