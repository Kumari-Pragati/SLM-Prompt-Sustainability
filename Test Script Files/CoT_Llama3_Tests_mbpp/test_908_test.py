import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):
    def test_found_fixed_point(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 0)

    def test_not_found_fixed_point(self):
        self.assertEqual(find_fixedPoint([0, 1, 2, 3, 4, 5, 6, 7, 8, 10], 10), -1)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            find_fixedPoint([], 0)

    def test_array_with_duplicates(self):
        self.assertEqual(find_fixedPoint([0, 1, 2, 3, 4, 5, 6, 7, 8, 8], 10), 8)

    def test_array_with_negative_numbers(self):
        self.assertEqual(find_fixedPoint([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 10), 0)

    def test_array_with_zero(self):
        self.assertEqual(find_fixedPoint([0, 1, 2, 3, 4, 5, 6, 7, 8, 0], 10), 0)
