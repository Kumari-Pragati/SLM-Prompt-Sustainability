import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 20, 4, 1, 0]
        n = len(arr)
        self.assertEqual(find_peak(arr, n), 2)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(find_peak(arr, n), 0)

    def test_peak_at_start(self):
        arr = [10, 8, 4, 2]
        n = len(arr)
        self.assertEqual(find_peak(arr, n), 0)

    def test_peak_at_end(self):
        arr = [2, 4, 8, 10]
        n = len(arr)
        self.assertEqual(find_peak(arr, n), 3)

    def test_no_peak(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        self.assertIsNone(find_peak(arr, n))

    def test_negative_numbers(self):
        arr = [-1, -3, -20, -4, -1, 0]
        n = len(arr)
        self.assertEqual(find_peak(arr, n), 3)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertIsNone(find_peak(arr, n))
