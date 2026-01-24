import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):

    def test_even_parity(self):
        self.assertTrue(check_Even_Parity(10))

    def test_odd_parity(self):
        self.assertFalse(check_Even_Parity(9))

    def test_zero_parity(self):
        self.assertTrue(check_Even_Parity(0))

    def test_negative_parity(self):
        self.assertFalse(check_Even_Parity(-10))

    def test_edge_case_parity(self):
        self.assertTrue(check_Even_Parity(1))

    def test_edge_case_parity2(self):
        self.assertFalse(check_Even_Parity(3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Even_Parity('a')
