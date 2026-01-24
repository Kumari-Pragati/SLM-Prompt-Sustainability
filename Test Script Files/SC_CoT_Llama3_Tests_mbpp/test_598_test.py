import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_armstrong_number_positive(self):
        self.assertTrue(armstrong_number(153))

    def test_armstrong_number_negative(self):
        self.assertFalse(armstrong_number(-153))

    def test_armstrong_number_zero(self):
        self.assertFalse(armstrong_number(0))

    def test_armstrong_number_single_digit(self):
        self.assertFalse(armstrong_number(1))

    def test_armstrong_number_non_armstrong(self):
        self.assertFalse(armstrong_number(123))

    def test_armstrong_number_armstrong(self):
        self.assertTrue(armstrong_number(153))

    def test_armstrong_number_armstrong_with_zero(self):
        self.assertTrue(armstrong_number(370))

    def test_armstrong_number_armstrong_with_single_digit(self):
        self.assertFalse(armstrong_number(1))

    def test_armstrong_number_invalid_input_type(self):
        with self.assertRaises(TypeError):
            armstrong_number("123")

    def test_armstrong_number_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            armstrong_number(12.3)
