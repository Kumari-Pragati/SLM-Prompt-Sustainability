import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_armstrong_number(self):
        self.assertTrue(armstrong_number(153))
        self.assertFalse(armstrong_number(123))
        self.assertFalse(armstrong_number(456))
        self.assertFalse(armstrong_number(1634))
        self.assertFalse(armstrong_number(0))
        self.assertFalse(armstrong_number(-123))
        self.assertFalse(armstrong_number(12000))

    def test_single_digit(self):
        self.assertTrue(armstrong_number(0))
        self.assertTrue(armstrong_number(1))
        self.assertTrue(armstrong_number(5))
        self.assertTrue(armstrong_number(9))

    def test_two_digits(self):
        self.assertTrue(armstrong_number(370))
        self.assertTrue(armstrong_number(371))
        self.assertFalse(armstrong_number(48))
        self.assertFalse(armstrong_number(75))

    def test_three_digits(self):
        self.assertTrue(armstrong_number(407))
        self.assertFalse(armstrong_number(152))
        self.assertFalse(armstrong_number(182))
        self.assertFalse(armstrong_number(271))
