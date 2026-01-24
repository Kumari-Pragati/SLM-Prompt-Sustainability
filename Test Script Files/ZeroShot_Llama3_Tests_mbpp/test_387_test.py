import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):

    def test_even(self):
        self.assertEqual(even_or_odd("10"), "Even")
        self.assertEqual(even_or_odd("20"), "Even")
        self.assertEqual(even_or_odd("30"), "Even")
        self.assertEqual(even_or_odd("40"), "Even")
        self.assertEqual(even_or_odd("50"), "Even")
        self.assertEqual(even_or_odd("60"), "Even")
        self.assertEqual(even_or_odd("70"), "Even")
        self.assertEqual(even_or_odd("80"), "Even")
        self.assertEqual(even_or_odd("90"), "Even")
        self.assertEqual(even_or_odd("A0"), "Even")
        self.assertEqual(even_or_odd("C0"), "Even")
        self.assertEqual(even_or_odd("E0"), "Even")

    def test_odd(self):
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("9"), "Odd")
        self.assertEqual(even_or_odd("B"), "Odd")
        self.assertEqual(even_or_odd("D"), "Odd")
        self.assertEqual(even_or_odd("F"), "Odd")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_or_odd("abc")
        with self.assertRaises(TypeError):
            even_or_odd(123)
