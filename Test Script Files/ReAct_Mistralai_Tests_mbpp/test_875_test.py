import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(TypeError, min_difference, [])

    def test_single_element_list(self):
        self.assertEqual(min_difference([1]), 0)

    def test_positive_numbers(self):
        self.assertEqual(min_difference([1, 2, 3]), 0)
        self.assertEqual(min_difference([1, 2, 3, 4]), 1)
        self.assertEqual(min_difference([1, 2, 3, 4, 5]), 1)

    def test_negative_numbers(self):
        self.assertEqual(min_difference([-1, -2, -3]), 1)
        self.assertEqual(min_difference([-1, -2, -3, -4]), 3)
        self.assertEqual(min_difference([-1, -2, -3, -4, -5]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(min_difference([1, -2, 3]), 1)
        self.assertEqual(min_difference([-1, 2, -3]), 3)
        self.assertEqual(min_difference([1, -2, 3, -4]), 1)
        self.assertEqual(min_difference([-1, 2, -3, 4]), 1)

    def test_duplicates(self):
        self.assertEqual(min_difference([1, 1, 2, 3]), 0)
        self.assertEqual(min_difference([-1, -1, -2, -3]), 2)
        self.assertEqual(min_difference([1, -1, 2, -2]), 1)
        self.assertEqual(min_difference([-1, 1, -2, 2]), 1)
