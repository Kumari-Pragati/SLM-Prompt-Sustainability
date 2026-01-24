import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_Diff([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Diff([1], 1), 0)

    def test_duplicates(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3], 5), 0)

    def test_single_duplicate(self):
        self.assertEqual(find_Diff([1, 1, 2, 3], 4), 1)

    def test_increasing_sequence(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 0)

    def test_decreasing_sequence(self):
        self.assertEqual(find_Diff([5, 4, 3, 2, 1], 5), 0)

    def test_alternating_sequence(self):
        self.assertEqual(find_Diff([1, 2, 3, 2, 1], 5), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_Diff([-1, -2, -3, -4, -5], 5), 0)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(ValueError):
            find_Diff([], "not_an_integer")

    def test_invalid_input_negative_number(self):
        with self.assertRaises(ValueError):
            find_Diff([1, 2, 3], -1)
