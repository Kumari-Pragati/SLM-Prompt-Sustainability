import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_digits_twoparts(1234), 18)

    def test_boundary_conditions(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(10), 1)
        self.assertEqual(sum_digits_twoparts(99), 18)

    def test_edge_conditions(self):
        self.assertEqual(sum_digits_twoparts(100), 1)
        self.assertEqual(sum_digits_twoparts(999), 18)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_digits_twoparts('1234')
        with self.assertRaises(ValueError):
            sum_digits_twoparts(-1234)
