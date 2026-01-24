import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(10, 20), (30, 40), (50, 60)]
        self.assertEqual(min_difference(test_list), 10)

    def test_single_element(self):
        test_list = [(10, 20)]
        self.assertEqual(min_difference(test_list), 10)

    def test_empty_list(self):
        test_list = []
        self.assertRaises(ValueError, min_difference, test_list)

    def test_negative_numbers(self):
        test_list = [(-10, 20), (-30, 40), (-50, 60)]
        self.assertEqual(min_difference(test_list), 70)

    def test_same_numbers(self):
        test_list = [(10, 10), (20, 20), (30, 30)]
        self.assertEqual(min_difference(test_list), 0)

    def test_large_numbers(self):
        test_list = [(1000000000, 2000000000), (3000000000, 4000000000), (5000000000, 6000000000)]
        self.assertEqual(min_difference(test_list), 1000000000)
