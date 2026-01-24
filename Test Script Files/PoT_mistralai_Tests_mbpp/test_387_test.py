import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_or_odd("0"), "Even")
        self.assertEqual(even_or_odd("2"), "Even")
        self.assertEqual(even_or_odd("4"), "Even")
        self.assertEqual(even_or_odd("6"), "Even")
        self.assertEqual(even_or_odd("8"), "Even")
        self.assertEqual(even_or_odd("A"), "Even")  # ASCII 'A' is 10 in decimal, which is even
        self.assertEqual(even_or_odd("C"), "Even")  # ASCII 'C' is 12 in decimal, which is even
        self.assertEqual(even_or_odd("E"), "Even")  # ASCII 'E' is 14 in decimal, which is even

    def test_odd(self):
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("9"), "Odd")
        self.assertEqual(even_or_odd("B"), "Odd")  # ASCII 'B' is 11 in decimal, which is odd
        self.assertEqual(even_or_odd("D"), "Odd")  # ASCII 'D' is 13 in decimal, which is odd
        self.assertEqual(even_or_odd("F"), "Odd")  # ASCII 'F' is 15 in decimal, which is odd

    def test_edge_cases(self):
        self.assertEqual(even_or_odd(""), "Odd")
        self.assertEqual(even_or_odd("00"), "Even")
        self.assertEqual(even_or_odd("10"), "Odd")
        self.assertEqual(even_or_odd("11"), "Odd")
        self.assertEqual(even_or_odd("99"), "Odd")
        self.assertEqual(even_or_odd("A0"), "Even")
        self.assertEqual(even_or_odd("AA"), "Even")
        self.assertEqual(even_or_odd("ZZ"), "Odd")
