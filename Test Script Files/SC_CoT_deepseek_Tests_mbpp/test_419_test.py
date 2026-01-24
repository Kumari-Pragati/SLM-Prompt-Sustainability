import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(round_and_sum([1.123, 2.345, 3.456]), 6.944)

    def test_single_element(self):
        self.assertAlmostEqual(round_and_sum([1.1]), 1.1)

    def test_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(round_and_sum([-1.123, -2.345, -3.456]), -6.944)

    def test_large_numbers(self):
        self.assertAlmostEqual(round_and_sum([1000000.123, 2000000.345, 3000000.456]), 6000000.944)

    def test_zero(self):
        self.assertEqual(round_and_sum([0, 0, 0]), 0)

    def test_decimal_zero(self):
        self.assertEqual(round_and_sum([0.0, 0.0, 0.0]), 0.0)

    def test_float_precision(self):
        self.assertAlmostEqual(round_and_sum([1.123456, 2.345678, 3.456789]), 6.944943)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            round_and_sum("1.123, 2.345, 3.456")

        with self.assertRaises(TypeError):
            round_and_sum(1.123, 2.345, 3.456)
