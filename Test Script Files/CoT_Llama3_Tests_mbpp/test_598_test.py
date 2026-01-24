import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):
    def test_armstrong_number_true(self):
        self.assertTrue(armstrong_number(153))

    def test_armstrong_number_false(self):
        self.assertFalse(armstrong_number(123))

    def test_armstrong_number_edge_case(self):
        self.assertTrue(armstrong_number(0))

    def test_armstrong_number_edge_case_negative(self):
        self.assertFalse(armstrong_number(-123))

    def test_armstrong_number_edge_case_single_digit(self):
        self.assertFalse(armstrong_number(1))

    def test_armstrong_number_edge_case_two_digits(self):
        self.assertFalse(armstrong_number(12))

    def test_armstrong_number_edge_case_three_digits(self):
        self.assertTrue(armstrong_number(153))

    def test_armstrong_number_edge_case_four_digits(self):
        self.assertFalse(armstrong_number(1234))

    def test_armstrong_number_edge_case_five_digits(self):
        self.assertFalse(armstrong_number(12345))

    def test_armstrong_number_invalid_input(self):
        with self.assertRaises(TypeError):
            armstrong_number("abc")
