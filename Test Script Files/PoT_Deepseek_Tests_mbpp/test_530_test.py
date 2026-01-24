import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(negative_count([1, -2, 3, -4, 5]), 0.4)

    def test_empty_list(self):
        self.assertEqual(negative_count([]), 0)

    def test_all_positive(self):
        self.assertEqual(negative_count([1, 2, 3, 4, 5]), 0)

    def test_all_negative(self):
        self.assertEqual(negative_count([-1, -2, -3, -4, -5]), 1)

    def test_all_zero(self):
        self.assertEqual(negative_count([0, 0, 0, 0, 0]), 0)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(negative_count([-1, 0, 1, -2, 2]), 0.4)

    def test_large_numbers(self):
        self.assertAlmostEqual(negative_count([100, -200, 300, -400, 500]), 0.4)
