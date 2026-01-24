import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_fixed_point([0, 2, 3, 4], 4), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_fixed_point([-1, -2, -3, -4], 4), -1)

    def test_no_fixed_point(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3], 4), -1)

    def test_empty_array(self):
        self.assertEqual(find_fixed_point([], 0), -1)

    def test_large_numbers(self):
        self.assertEqual(find_fixed_point([100000, 199999, 299998, 399997], 4), -1)

    def test_duplicate_values(self):
        self.assertEqual(find_fixed_point([0, 0, 1, 2], 4), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_fixed_point("not an array", 1)
