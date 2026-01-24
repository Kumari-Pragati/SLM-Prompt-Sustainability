import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(even_or_odd("0"), "Even")
        self.assertEqual(even_or_odd("10"), "Even")
        self.assertEqual(even_or_odd("12"), "Even")
        self.assertEqual(even_or_odd("14"), "Even")
        self.assertEqual(even_or_odd("16"), "Even")
        self.assertEqual(even_or_odd("18"), "Even")
        self.assertEqual(even_or_odd("1A"), "Even")
        self.assertEqual(even_or_odd("20"), "Even")
        self.assertEqual(even_or_odd("22"), "Even")
        self.assertEqual(even_or_odd("24"), "Even")
        self.assertEqual(even_or_odd("26"), "Even")
        self.assertEqual(even_or_odd("28"), "Even")
        self.assertEqual(even_or_odd("2E"), "Even")
        self.assertEqual(even_or_odd("30"), "Even")

    def test_odd_number(self):
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("9"), "Odd")
        self.assertEqual(even_or_odd("B"), "Odd")
        self.assertEqual(even_or_odd("D"), "Odd")
        self.assertEqual(even_or_odd("F"), "Odd")
        self.assertEqual(even_or_odd("G"), "Odd")
        self.assertEqual(even_or_odd("H"), "Odd")

    def test_empty_string(self):
        self.assertEqual(even_or_odd(""), "Error: Invalid input")

    def test_single_digit(self):
        self.assertEqual(even_or_odd("0"), "Even")
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("2"), "Even")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("4"), "Even")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("6"), "Even")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("8"), "Even")
        self.assertEqual(even_or_odd("9"), "Odd")

    def test_single_digit_uppercase(self):
        self.assertEqual(even_or_odd("A"), "Even")
        self.assertEqual(even_or_odd("B"), "Odd")
        self.assertEqual(even_or_odd("C"), "Even")
        self.assertEqual(even_or_odd("D"), "Odd")
        self.assertEqual(even_or_odd("E"), "Even")
        self.assertEqual(even_or_odd("F"), "Odd")
