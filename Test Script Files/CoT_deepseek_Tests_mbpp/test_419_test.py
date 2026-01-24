import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(round_and_sum([1.123, 2.345, 3.456]), 6.934)

    def test_single_element(self):
        self.assertAlmostEqual(round_and_sum([1.1]), 1.1)

    def test_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(round_and_sum([-1.123, -2.345, -3.456]), -6.934)

    def test_zeroes(self):
        self.assertEqual(round_and_sum([0, 0, 0]), 0)

    def test_large_numbers(self):
        self.assertAlmostEqual(round_and_sum([1000000.123, 2000000.345, 3000000.456]), 6000000.934)

    def test_decimal_places(self):
        self.assertAlmostEqual(round_and_sum([1.12345, 2.34567, 3.45678]), 6.93481)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            round_and_sum([1.1, 'two', 3.3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            round_and_sum(12345)
