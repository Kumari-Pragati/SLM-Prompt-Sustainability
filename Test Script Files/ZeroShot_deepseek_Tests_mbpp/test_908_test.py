import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_fixed_point([0, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_fixed_point([-10, -5, 0, 3, 7], 5), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_fixed_point([-10, -5, 3, 4, 7], 5), -1)

    def test_mixed_numbers(self):
        self.assertEqual(find_fixed_point([-1, 0, 2, 3, 9], 5), -1)

    def test_empty_array(self):
        self.assertEqual(find_fixed_point([], 0), -1)

    def test_single_element(self):
        self.assertEqual(find_fixed_point([0], 1), 0)
