import unittest
from768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_Odd_Parity(1))
        self.assertTrue(check_Odd_Parity(3))
        self.assertTrue(check_Odd_Parity(5))
        self.assertFalse(check_Odd_Parity(0))
        self.assertFalse(check_Odd_Parity(2))
        self.assertFalse(check_Odd_Parity(4))

    def test_edge_cases(self):
        self.assertTrue(check_Odd_Parity(-1))
        self.assertTrue(check_Odd_Parity(2 ** 31 - 1))
        self.assertFalse(check_Odd_Parity(2 ** 31))
