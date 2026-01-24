import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_or_odd("0"), "Even")
        self.assertEqual(even_or_odd("2"), "Even")
        self.assertEqual(even_or_odd("4"), "Even")
        self.assertEqual(even_or_odd("6"), "Even")
        self.assertEqual(even_or_odd("8"), "Even")
        self.assertEqual(even_or_odd("A"), "Even")
        self.assertEqual(even_or_odd("C"), "Even")
        self.assertEqual(even_or_odd("E"), "Even")

    def test_odd(self):
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("9"), "Odd")
        self.assertEqual(even_or_odd("B"), "Odd")
        self.assertEqual(even_or_odd("D"), "Odd")
        self.assertEqual(even_or_odd("F"), "Odd")

    def test_empty(self):
        with self.assertRaises(TypeError):
            even_or_odd("")

    def test_non_string(self):
        with self.assertRaises(TypeError):
            even_or_odd(123)

    def test_multiple_digits(self):
        self.assertEqual(even_or_odd("10"), "Even")
        self.assertEqual(even_or_odd("12"), "Even")
        self.assertEqual(even_or_odd("14"), "Even")
        self.assertEqual(even_or_odd("16"), "Even")
        self.assertEqual(even_or_odd("18"), "Even")
        self.assertEqual(even_or_odd("20"), "Even")

    def test_single_digit(self):
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("2"), "Even")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("4"), "Even")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("6"), "Even")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("8"), "Even")
        self.assertEqual(even_or_odd("9"), "Odd")
