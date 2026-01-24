import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):

    def test_single_digit_armstrong_numbers(self):
        self.assertTrue(armstrong_number(0))
        self.assertTrue(armstrong_number(1))
        self.assertTrue(armstrong_number(2))
        self.assertTrue(armstrong_number(3))
        self.assertTrue(armstrong_number(4))
        self.assertTrue(armstrong_number(5))
        self.assertTrue(armstrong_number(6))
        self.assertTrue(armstrong_number(7))
        self.assertTrue(armstrong_number(8))
        self.assertTrue(armstrong_number(9))

    def test_double_digit_armstrong_numbers(self):
        self.assertTrue(armstrong_number(153))
        self.assertTrue(armstrong_number(370))
        self.assertTrue(armstrong_number(371))
        self.assertTrue(armstrong_number(407))

    def test_triple_digit_armstrong_numbers(self):
        self.assertTrue(armstrong_number(9474))
        self.assertTrue(armstrong_number(9475))

    def test_non_armstrong_numbers(self):
        self.assertFalse(armstrong_number(100))
        self.assertFalse(armstrong_number(101))
        self.assertFalse(armstrong_number(123))
        self.assertFalse(armstrong_number(124))

    def test_negative_numbers(self):
        self.assertFalse(armstrong_number(-1))
        self.assertFalse(armstrong_number(-123))

    def test_large_numbers(self):
        self.assertFalse(armstrong_number(1000000000000000000))
