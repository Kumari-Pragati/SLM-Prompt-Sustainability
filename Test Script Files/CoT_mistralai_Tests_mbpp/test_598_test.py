import unittest
from598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertTrue(armstrong_number(153))
        self.assertFalse(armstrong_number(123))
        self.assertFalse(armstrong_number(0))
        self.assertFalse(armstrong_number(-123))
        self.assertTrue(armstrong_number(370))
        self.assertTrue(armstrong_number(371))
        self.assertFalse(armstrong_number(372))
        self.assertFalse(armstrong_number(407))

    def test_single_digit(self):
        for num in range(1, 10):
            self.assertTrue(armstrong_number(num))

    def test_large_number(self):
        large_num = 1000000
        self.assertFalse(armstrong_number(large_num))
