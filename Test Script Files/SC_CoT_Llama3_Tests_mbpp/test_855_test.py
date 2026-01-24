import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):
    def test_even_parity(self):
        self.assertTrue(check_Even_Parity(10))
        self.assertFalse(check_Even_Parity(9))
        self.assertTrue(check_Even_Parity(8))
        self.assertFalse(check_Even_Parity(7))
        self.assertTrue(check_Even_Parity(6))
        self.assertFalse(check_Even_Parity(5))
        self.assertTrue(check_Even_Parity(4))
        self.assertFalse(check_Even_Parity(3))
        self.assertTrue(check_Even_Parity(2))
        self.assertFalse(check_Even_Parity(1))
        self.assertFalse(check_Even_Parity(0))

    def test_zero(self):
        self.assertFalse(check_Even_Parity(0))

    def test_negative(self):
        self.assertFalse(check_Even_Parity(-1))
        self.assertFalse(check_Even_Parity(-2))
        self.assertFalse(check_Even_Parity(-3))
        self.assertFalse(check_Even_Parity(-4))
        self.assertFalse(check_Even_Parity(-5))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            check_Even_Parity(10.5)
        with self.assertRaises(TypeError):
            check_Even_Parity('10')
