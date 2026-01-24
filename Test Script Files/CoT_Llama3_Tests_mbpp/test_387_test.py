import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(even_or_odd("0"), "Even")
        self.assertEqual(even_or_odd("2"), "Even")
        self.assertEqual(even_or_odd("4"), "Even")
        self.assertEqual(even_or_odd("6"), "Even")
        self.assertEqual(even_or_odd("8"), "Even")
        self.assertEqual(even_or_odd("A"), "Even")
        self.assertEqual(even_or_odd("C"), "Even")
        self.assertEqual(even_or_odd("E"), "Even")

    def test_odd_numbers(self):
        self.assertEqual(even_or_odd("1"), "Odd")
        self.assertEqual(even_or_odd("3"), "Odd")
        self.assertEqual(even_or_odd("5"), "Odd")
        self.assertEqual(even_or_odd("7"), "Odd")
        self.assertEqual(even_or_odd("9"), "Odd")
        self.assertEqual(even_or_odd("B"), "Odd")
        self.assertEqual(even_or_odd("D"), "Odd")
        self.assertEqual(even_or_odd("F"), "Odd")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_or_odd(123)
        with self.assertRaises(TypeError):
            even_or_odd("Invalid")
        with self.assertRaises(TypeError):
            even_or_odd([1, 2, 3])
