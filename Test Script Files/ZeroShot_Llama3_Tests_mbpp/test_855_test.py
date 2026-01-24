import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):

    def test_even_parity(self):
        self.assertTrue(check_Even_Parity(10))
        self.assertTrue(check_Even_Parity(20))
        self.assertTrue(check_Even_Parity(30))
        self.assertTrue(check_Even_Parity(40))
        self.assertTrue(check_Even_Parity(50))

    def test_odd_parity(self):
        self.assertFalse(check_Even_Parity(9))
        self.assertFalse(check_Even_Parity(19))
        self.assertFalse(check_Even_Parity(29))
        self.assertFalse(check_Even_Parity(39))
        self.assertFalse(check_Even_Parity(49))

    def test_edge_cases(self):
        self.assertTrue(check_Even_Parity(0))
        self.assertFalse(check_Even_Parity(1))
