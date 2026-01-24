import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_simple_cases(self):
        self.assertTrue(check_Odd_Parity(7))
        self.assertFalse(check_Odd_Parity(6))

    def test_edge_conditions(self):
        self.assertTrue(check_Odd_Parity(1))
        self.assertFalse(check_Odd_Parity(0))
        self.assertFalse(check_Odd_Parity(2))

    def test_boundary_conditions(self):
        self.assertTrue(check_Odd_Parity(2**31 - 1))
        self.assertFalse(check_Odd_Parity(2**31))

    def test_complex_cases(self):
        self.assertTrue(check_Odd_Parity(7777))
        self.assertFalse(check_Odd_Parity(8888))
