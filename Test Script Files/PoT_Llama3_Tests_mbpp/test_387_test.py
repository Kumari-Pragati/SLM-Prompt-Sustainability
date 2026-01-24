import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_typical_even(self):
        self.assertEqual(even_or_odd("10"), "Even")

    def test_typical_odd(self):
        self.assertEqual(even_or_odd("11"), "Odd")

    def test_edge_case_zero(self):
        self.assertEqual(even_or_odd("0"), "Even")

    def test_edge_case_last_digit_zero(self):
        self.assertEqual(even_or_odd("1230"), "Even")

    def test_edge_case_last_digit_non_zero(self):
        self.assertEqual(even_or_odd("1231"), "Odd")

    def test_edge_case_last_digit_A(self):
        self.assertEqual(even_or_odd("123A"), "Even")

    def test_edge_case_last_digit_non_zero_non_hex(self):
        self.assertEqual(even_or_odd("1237"), "Odd")

    def test_edge_case_last_digit_C(self):
        self.assertEqual(even_or_odd("123C"), "Even")

    def test_edge_case_last_digit_E(self):
        self.assertEqual(even_or_odd("123E"), "Even")

    def test_edge_case_last_digit_non_zero_non_hex_non_zero(self):
        self.assertEqual(even_or_odd("1239"), "Odd")
