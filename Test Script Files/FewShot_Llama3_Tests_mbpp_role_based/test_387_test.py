import unittest
from mbpp_387_code import even_or_odd

class TestEvenOrOdd(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(even_or_odd("10"), "Even")

    def test_odd_number(self):
        self.assertEqual(even_or_odd("11"), "Odd")

    def test_even_number_with_last_digit_zero(self):
        self.assertEqual(even_or_odd("20"), "Even")

    def test_even_number_with_last_digit_two(self):
        self.assertEqual(even_or_odd("22"), "Even")

    def test_odd_number_with_last_digit_one(self):
        self.assertEqual(even_or_odd("13"), "Odd")

    def test_odd_number_with_last_digit_five(self):
        self.assertEqual(even_or_odd("15"), "Odd")

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            even_or_odd("abc")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            even_or_odd(123)
