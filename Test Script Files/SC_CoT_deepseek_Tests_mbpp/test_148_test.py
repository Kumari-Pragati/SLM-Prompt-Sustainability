import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_digits_twoparts(12345), 15)
        self.assertEqual(sum_digits_twoparts(98765), 30)

    def test_edge_cases(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(10), 1)
        self.assertEqual(sum_digits_twoparts(99), 18)

    def test_boundary_cases(self):
        self.assertEqual(sum_digits_twoparts(100), 1)
        self.assertEqual(sum_digits_twoparts(999), 18)

    def test_corner_cases(self):
        self.assertEqual(sum_digits_twoparts(1000), 1)
        self.assertEqual(sum_digits_twoparts(9999), 18)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_digits_twoparts('12345')
        with self.assertRaises(ValueError):
            sum_digits_twoparts(-12345)
