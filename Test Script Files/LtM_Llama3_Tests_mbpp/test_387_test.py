import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_simple_even(self):
        self.assertEqual(even_or_odd("0"), "Even")

    def test_simple_odd(self):
        self.assertEqual(even_or_odd("1"), "Odd")

    def test_edge_case_zero(self):
        self.assertEqual(even_or_odd("0"), "Even")

    def test_edge_case_max(self):
        self.assertEqual(even_or_odd("9"), "Odd")

    def test_edge_case_alpha(self):
        self.assertEqual(even_or_odd("A"), "Even")

    def test_edge_case_max_alpha(self):
        self.assertEqual(even_or_odd("9A"), "Odd")

    def test_edge_case_min_alpha(self):
        self.assertEqual(even_or_odd("0A"), "Even")

    def test_edge_case_max_alpha_zero(self):
        self.assertEqual(even_or_odd("9A0"), "Odd")

    def test_edge_case_min_alpha_zero(self):
        self.assertEqual(even_or_odd("0A0"), "Even")

    def test_edge_case_max_alpha_zero_odd(self):
        self.assertEqual(even_or_odd("9A0A"), "Odd")

    def test_edge_case_min_alpha_zero_even(self):
        self.assertEqual(even_or_odd("0A0A"), "Even")
