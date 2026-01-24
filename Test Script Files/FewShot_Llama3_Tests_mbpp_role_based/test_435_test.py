import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(last_Digit(123), 3)

    def test_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(last_Digit(-123), 3)

    def test_large_numbers(self):
        self.assertEqual(last_Digit(123456789), 9)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            last_Digit("123")
