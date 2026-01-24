import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(armstrong_number(153))

    def test_single_digit_number(self):
        self.assertTrue(armstrong_number(0))
        self.assertTrue(armstrong_number(9))

    def test_two_digit_armstrong_number(self):
        self.assertTrue(armstrong_number(1634))

    def test_three_digit_armstrong_number(self):
        self.assertTrue(armstrong_number(371))

    def test_four_digit_armstrong_number(self):
        self.assertTrue(armstrong_number(407))

    def test_negative_number(self):
        self.assertFalse(armstrong_number(-153))

    def test_zero(self):
        self.assertTrue(armstrong_number(0))

    def test_large_number(self):
        self.assertFalse(armstrong_number(1000000000000000000))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            armstrong_number(153.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            armstrong_number("153")

    def test_list_input(self):
        with self.assertRaises(TypeError):
            armstrong_number([153])
