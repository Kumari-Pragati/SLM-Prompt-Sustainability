import unittest
from768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_one(self):
        self.assertTrue(check_Odd_Parity(1))

    def test_even_numbers(self):
        for i in range(2, 10):
            self.assertFalse(check_Odd_Parity(i))

    def test_odd_numbers(self):
        for i in range(1, 10):
            self.assertTrue(check_Odd_Parity(i * 2 + 1))
