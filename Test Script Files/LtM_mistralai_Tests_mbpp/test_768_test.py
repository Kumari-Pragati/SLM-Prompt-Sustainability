import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_simple_odd(self):
        self.assertTrue(check_Odd_Parity(1))
        self.assertTrue(check_Odd_Parity(3))
        self.assertTrue(check_Odd_Parity(5))

    def test_simple_even(self):
        self.assertFalse(check_Odd_Parity(0))
        self.assertFalse(check_Odd_Parity(2))
        self.assertFalse(check_Odd_Parity(4))

    def test_edge_cases(self):
        self.assertTrue(check_Odd_Parity(2147483647))
        self.assertTrue(check_Odd_Parity(-2147483647))
        self.assertFalse(check_Odd_Parity(-1))

    def test_complex_cases(self):
        self.assertTrue(check_Odd_Parity(0b10000000000000000000000000000001))
        self.assertFalse(check_Odd_Parity(0b10000000000000000000000000000010))
