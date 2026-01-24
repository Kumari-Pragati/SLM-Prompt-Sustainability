import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max([1, 3, 5, 7, 9], 0, 4), 9)

    def test_single_element(self):
        self.assertEqual(find_Max([5], 0, 0), 5)

    def test_sorted_descending(self):
        self.assertEqual(find_Max([9, 7, 5, 3, 1], 0, 4), 1)

    def test_sorted_ascending(self):
        self.assertEqual(find_Max([1, 3, 5, 7, 9], 0, 4), 9)

    def test_duplicate_max(self):
        self.assertEqual(find_Max([1, 3, 5, 7, 7], 0, 4), 7)

    def test_low_greater_than_high(self):
        self.assertEqual(find_Max([1, 3, 5, 7, 9], 5, 0), 1)

    def test_low_equals_high(self):
        self.assertEqual(find_Max([5], 0, 0), 5)

    def test_low_less_than_zero(self):
        with self.assertRaises(IndexError):
            find_Max([1, 3, 5, 7, 9], -1, 4)

    def test_high_greater_than_length(self):
        with self.assertRaises(IndexError):
            find_Max([1, 3, 5, 7, 9], 0, 6)
