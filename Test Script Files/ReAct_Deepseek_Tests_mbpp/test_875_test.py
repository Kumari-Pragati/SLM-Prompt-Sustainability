import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(min_difference([(10, 20), (30, 40), (50, 60)]), 10)

    def test_single_element(self):
        self.assertEqual(min_difference([(10, 10)]), 0)

    def test_empty_list(self):
        self.assertIsNone(min_difference([]))

    def test_negative_numbers(self):
        self.assertAlmostEqual(min_difference([(-10, 10), (-20, 20), (-30, 30)]), 40)

    def test_zero_difference(self):
        self.assertEqual(min_difference([(0, 0)]), 0)

    def test_large_numbers(self):
        self.assertAlmostEqual(min_difference([(1000000, 2000000), (3000000, 4000000), (5000000, 6000000)]), 1000000)

    def test_float_numbers(self):
        self.assertAlmostEqual(min_difference([(10.5, 20.5), (30.5, 40.5), (50.5, 60.5)]), 10.0)
