import unittest
from mbpp_383_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_even_bit_toggle_number_positive(self):
        self.assertEqual(even_bit_toggle_number(10), 10)

    def test_even_bit_toggle_number_negative(self):
        self.assertEqual(even_bit_toggle_number(-10), -10)

    def test_even_bit_toggle_number_zero(self):
        self.assertEqual(even_bit_toggle_number(0), 0)

    def test_even_bit_toggle_number_power_of_two(self):
        self.assertEqual(even_bit_toggle_number(8), 8)

    def test_even_bit_toggle_number_power_of_two_negative(self):
        self.assertEqual(even_bit_toggle_number(-8), -8)

    def test_even_bit_toggle_number_non_power_of_two(self):
        self.assertEqual(even_bit_toggle_number(15), 15)

    def test_even_bit_toggle_number_non_power_of_two_negative(self):
        self.assertEqual(even_bit_toggle_number(-15), -15)

    def test_even_bit_toggle_number_edge_case(self):
        self.assertEqual(even_bit_toggle_number(1), 1)

    def test_even_bit_toggle_number_edge_case_negative(self):
        self.assertEqual(even_bit_toggle_number(-1), -1)
