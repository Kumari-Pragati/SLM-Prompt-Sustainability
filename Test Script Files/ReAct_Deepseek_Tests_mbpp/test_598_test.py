import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(armstrong_number(153))
        self.assertTrue(armstrong_number(370))
        self.assertTrue(armstrong_number(9474))

    def test_single_digit_numbers(self):
        for i in range(10):
            self.assertTrue(armstrong_number(i))

    def test_zero(self):
        self.assertTrue(armstrong_number(0))

    def test_negative_numbers(self):
        self.assertFalse(armstrong_number(-153))

    def test_large_numbers(self):
        self.assertFalse(armstrong_number(10000000000000000))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            armstrong_number(153.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            armstrong_number("153")

    def test_list_input(self):
        with self.assertRaises(TypeError):
            armstrong_number([153])
