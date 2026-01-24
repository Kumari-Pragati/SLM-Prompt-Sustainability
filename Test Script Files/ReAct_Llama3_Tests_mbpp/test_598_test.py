import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_armstrong_number_typical_case(self):
        self.assertTrue(armstrong_number(153))

    def test_armstrong_number_edge_case(self):
        self.assertFalse(armstrong_number(10))

    def test_armstrong_number_zero(self):
        self.assertFalse(armstrong_number(0))

    def test_armstrong_number_negative(self):
        self.assertFalse(armstrong_number(-10))

    def test_armstrong_number_non_armstrong(self):
        self.assertFalse(armstrong_number(123))

    def test_armstrong_number_armstrong(self):
        self.assertTrue(armstrong_number(371))

    def test_armstrong_number_invalid_input(self):
        with self.assertRaises(TypeError):
            armstrong_number('abc')
