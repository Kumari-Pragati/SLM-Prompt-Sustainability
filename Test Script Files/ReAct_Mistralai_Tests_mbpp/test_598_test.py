import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_armstrong_number_positive_integer(self):
        self.assertTrue(armstrong_number(153))
        self.assertTrue(armstrong_number(370))
        self.assertTrue(armstrong_number(371))  # Edge case: one off from perfect armstrong

    def test_armstrong_number_zero(self):
        self.assertFalse(armstrong_number(0))

    def test_armstrong_number_negative_integer(self):
        self.assertFalse(armstrong_number(-153))

    def test_armstrong_number_floats(self):
        self.assertFalse(armstrong_number(3.14))
        self.assertFalse(armstrong_number(278.0))

    def test_armstrong_number_non_integer(self):
        self.assertFalse(armstrong_number('abc'))
        self.assertFalse(armstrong_number([1, 2, 3]))
