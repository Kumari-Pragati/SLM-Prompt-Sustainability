import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_even_numbers(self):
        self.assertFalse(check_Odd_Parity(10))

    def test_odd_numbers(self):
        self.assertTrue(check_Odd_Parity(11))

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_negative_numbers(self):
        self.assertTrue(check_Odd_Parity(-11))

    def test_large_numbers(self):
        self.assertTrue(check_Odd_Parity(1000001))

    def test_small_numbers(self):
        self.assertTrue(check_Odd_Parity(3))

    def test_edge_case(self):
        self.assertFalse(check_Odd_Parity(2))
