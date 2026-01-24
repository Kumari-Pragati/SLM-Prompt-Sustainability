import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 4), 3.5)

    def test_empty_arrays(self):
        self.assertIsNone(get_median([], [], 0))
        self.assertIsNone(get_median([], [], 1))

    def test_single_array(self):
        self.assertEqual(get_median([1, 3, 5], [], 3), 3)
        self.assertEqual(get_median([], [1, 3, 5], 3), 3)

    def test_odd_length_arrays(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 4), 3.5)

    def test_even_length_arrays(self):
        self.assertEqual(get_median([1, 3, 5, 7], [2, 4, 6, 8], 4), 4.5)
        self.assertEqual(get_median([1, 3, 5, 7], [2, 4, 6, 8], 5), 4.5)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_median([1, 3, 5], [2, 4, 6], -1)
        with self.assertRaises(ValueError):
            get_median([1, 3, 5], [2, 4, 6], n=0)
