import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_simple_even(self):
        self.assertEqual(even_or_odd("0"), "Even")
        self.assertEqual(even_or_odd("8"), "Even")
        self.assertEqual(even_or_odd("A"), "Even")
        self.assertEqual(even_or_odd("C"), "Even")
        self.assertEqual(even_or_odd("E"), "Even")

    def test_simple_odd(self):
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("D"), "Odd")
        self.assertEqual(even_or_odd("F"), "Odd")
        self.assertEqual(even_or_odd("G"), "Odd")
        self.assertEqual(even_or_odd("9"), "Odd")

    def test_edge_cases(self):
        self.assertEqual(even_or_odd(""), "Odd")
        self.assertEqual(even_or_odd("99"), "Odd")
        self.assertEqual(even_or_odd("00"), "Even")
        self.assertEqual(even_or_odd("A9"), "Even")
        self.assertEqual(even_or_odd("C9"), "Even")
        self.assertEqual(even_or_odd("E9"), "Even")

    def test_complex_cases(self):
        self.assertEqual(even_or_odd("01"), "Even")
        self.assertEqual(even_or_odd("10"), "Odd")
        self.assertEqual(even_or_odd("0A"), "Even")
        self.assertEqual(even_or_odd("A0"), "Even")
        self.assertEqual(even_or_odd("0C"), "Even")
        self.assertEqual(even_or_odd("C0"), "Even")
        self.assertEqual(even_or_odd("0E"), "Even")
        self.assertEqual(even_or_odd("E0"), "Even")
