import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):

    def test_even_single_digit(self):
        self.assertEqual(even_or_odd("2"), "Even")
        self.assertEqual(even_or_odd("4"), "Even")
        self.assertEqual(even_or_odd("0"), "Even")
        self.assertEqual(even_or_odd("6"), "Even")
        self.assertEqual(even_or_odd("8"), "Even")

    def test_even_multiple_digits(self):
        self.assertEqual(even_or_odd("10"), "Even")
        self.assertEqual(even_or_odd("12"), "Even")
        self.assertEqual(even_or_odd("14"), "Even")
        self.assertEqual(even_or_odd("16"), "Even")
        self.assertEqual(even_or_odd("18"), "Even")

    def test_odd_single_digit(self):
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("9"), "Odd")

    def test_odd_multiple_digits(self):
        self.assertEqual(even_or_odd("21"), "Odd")
        self.assertEqual(even_or_odd("23"), "Odd")
        self.assertEqual(even_or_odd("25"), "Odd")
        self.assertEqual(even_or_odd("27"), "Odd")
        self.assertEqual(even_or_odd("29"), "Odd")

    def test_edge_cases(self):
        self.assertEqual(even_or_odd("A"), "Even")
        self.assertEqual(even_or_odd("C"), "Even")
        self.assertEqual(even_or_odd("E"), "Even")

        self.assertEqual(even_or_odd("1A"), "Odd")
        self.assertEqual(even_or_odd("C1"), "Odd")
        self.assertEqual(even_or_odd("E1"), "Odd")

        self.assertEqual(even_or_odd("00"), "Even")
        self.assertEqual(even_or_odd("99"), "Odd")
