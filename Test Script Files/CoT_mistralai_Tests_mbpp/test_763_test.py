import unittest
from763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_Min_Diff([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Min_Diff([1], 1), 0)

    def test_duplicates(self):
        self.assertEqual(find_Min_Diff([1, 1, 2], 3), 0)

    def test_increasing_sequence(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4], 4), 1)

    def test_decreasing_sequence(self):
        self.assertEqual(find_Min_Diff([4, 3, 2, 1], 4), 1)

    def test_random_sequence(self):
        self.assertEqual(find_Min_Diff([3, 1, 5, 4, 2], 5), 1)

    def test_large_sequence(self):
        arr = [i for i in range(1000)]
        self.assertEqual(find_Min_Diff(arr, len(arr)), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Diff([-1, -2, -3], 3), 1)

    def test_invalid_input_empty_array(self):
        with self.assertRaises(ValueError):
            find_Min_Diff([], "not_an_integer")

    def test_invalid_input_negative_n(self):
        with self.assertRaises(ValueError):
            find_Min_Diff([1, 2, 3], -1)
