import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_Odd_Parity(5))
        self.assertFalse(check_Odd_Parity(4))

    def test_edge_case_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_edge_case_one(self):
        self.assertFalse(check_Odd_Parity(1))

    def test_edge_case_negative(self):
        self.assertFalse(check_Odd_Parity(-1))
        self.assertFalse(check_Odd_Parity(-5))

    def test_edge_case_large(self):
        self.assertTrue(check_Odd_Parity(1001))
        self.assertFalse(check_Odd_Parity(1000))

    def test_edge_case_negative_large(self):
        self.assertFalse(check_Odd_Parity(-1000))
        self.assertFalse(check_Odd_Parity(-1001))
