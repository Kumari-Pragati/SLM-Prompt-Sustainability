import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_Odd_Parity(7))
        self.assertFalse(check_Odd_Parity(8))
        self.assertTrue(check_Odd_Parity(15))
        self.assertFalse(check_Odd_Parity(16))

    def test_edge_cases(self):
        self.assertFalse(check_Odd_Parity(0))
        self.assertFalse(check_Odd_Parity(-1))
        self.assertFalse(check_Odd_Parity(-2))

    def test_boundary_cases(self):
        self.assertTrue(check_Odd_Parity(2**31 - 1))
        self.assertFalse(check_Odd_Parity(2**31))
