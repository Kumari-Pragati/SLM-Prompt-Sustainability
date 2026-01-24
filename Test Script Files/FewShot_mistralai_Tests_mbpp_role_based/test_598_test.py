import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertTrue(armstrong_number(153))
        self.assertFalse(armstrong_number(123))
        self.assertFalse(armstrong_number(0))
        self.assertFalse(armstrong_number(1024))
        self.assertFalse(armstrong_number(-1))
