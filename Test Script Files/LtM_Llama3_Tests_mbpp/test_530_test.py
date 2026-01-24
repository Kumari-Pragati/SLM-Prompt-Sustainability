import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):
    def test_zero_negative(self):
        self.assertEqual(negative_count([0, 0, 0]), 0)

    def test_one_negative(self):
        self.assertAlmostEqual(negative_count([0, 0, -1]), 0.3333333333333333)

    def test_multiple_negative(self):
        self.assertAlmostEqual(negative_count([-1, -2, -3, 0, 0, 0]), 0.6666666666666666)

    def test_empty_list(self):
        self.assertEqual(negative_count([]), 0)

    def test_all_positive(self):
        self.assertEqual(negative_count([1, 2, 3]), 0)

    def test_all_negative(self):
        self.assertAlmostEqual(negative_count([-1, -2, -3]), 1.0)

    def test_mixed(self):
        self.assertAlmostEqual(negative_count([-1, 0, 1, -2, 3]), 0.5)
