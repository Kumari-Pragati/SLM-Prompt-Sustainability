import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 4), 1)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 1), 0)

    def test_empty_list(self):
        self.assertEqual(find_Min_Diff([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Min_Diff([1], 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Diff([-1, -2, -3, -4, -5], 5), 1)
        self.assertEqual(find_Min_Diff([-1, -2, -3, -4, -5], 4), 1)
        self.assertEqual(find_Min_Diff([-1, -2, -3, -4, -5], 2), 3)
        self.assertEqual(find_Min_Diff([-1, -2, -3, -4, -5], 1), 0)

    def test_duplicates(self):
        self.assertEqual(find_Min_Diff([1, 1, 2, 3], 4), 0)
        self.assertEqual(find_Min_Diff([1, 1, 2, 3], 3), 0)
        self.assertEqual(find_Min_Diff([1, 1, 2, 3], 2), 1)
        self.assertEqual(find_Min_Diff([1, 1, 2, 3], 1), 0)

    def test_invalid_input_length(self):
        self.assertRaises(ValueError, find_Min_Diff, [], -1)
        self.assertRaises(ValueError, find_Min_Diff, [1], -1)
        self.assertRaises(ValueError, find_Min_Diff, [1, 2], 0)
        self.assertRaises(ValueError, find_Min_Diff, [1, 2], -1)
