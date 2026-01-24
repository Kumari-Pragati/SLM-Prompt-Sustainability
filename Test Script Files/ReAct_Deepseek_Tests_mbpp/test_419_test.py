import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(round_and_sum([1.123, 2.345, 3.456]), 11)

    def test_single_number(self):
        self.assertEqual(round_and_sum([1.0]), 1)

    def test_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.123, -2.345, -3.456]), -11)

    def test_zeroes(self):
        self.assertEqual(round_and_sum([0, 0, 0]), 0)

    def test_large_numbers(self):
        self.assertEqual(round_and_sum([1000000.123, 2000000.345, 3000000.456]), 6000001)

    def test_decimal_numbers(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 6)

    def test_integer_numbers(self):
        self.assertEqual(round_and_sum([1, 2, 3]), 6)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            round_and_sum([1, 'a', 2])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            round_and_sum(123)
