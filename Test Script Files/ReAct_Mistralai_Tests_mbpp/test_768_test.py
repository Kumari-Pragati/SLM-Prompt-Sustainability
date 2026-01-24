import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_positive_odd_numbers(self):
        self.assertTrue(check_Odd_Parity(1))
        self.assertTrue(check_Odd_Parity(3))
        self.assertTrue(check_Odd_Parity(5))
        self.assertTrue(check_Odd_Parity(7))

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_negative_numbers(self):
        self.assertTrue(check_Odd_Parity(-1))
        self.assertFalse(check_Odd_Parity(-2))
        self.assertTrue(check_Odd_Parity(-3))
        self.assertFalse(check_Odd_Parity(-4))

    def test_edge_cases(self):
        self.assertTrue(check_Odd_Parity(1 << 31 - 1))  # max positive int
        self.assertFalse(check_Odd_Parity(1 << 31))  # max positive int - 1
        self.assertFalse(check_Odd_Parity(-(1 << 31)))  # max negative int
        self.assertTrue(check_Odd_Parity(-(1 << 31) + 1))  # max negative int + 1
