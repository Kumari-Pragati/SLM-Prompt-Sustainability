import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_digits_twoparts(1234), 10)
        self.assertEqual(sum_digits_twoparts(9876), 36)

    def test_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(10), 1)

    def test_boundary_cases(self):
        self.assertEqual(sum_digits_twoparts(10000), 1)
        self.assertEqual(sum_digits_twoparts(99999), 45)

    def test_corner_cases(self):
        self.assertEqual(sum_digits_twoparts(100000), 1)
        self.assertEqual(sum_digits_twoparts(999999), 45)
