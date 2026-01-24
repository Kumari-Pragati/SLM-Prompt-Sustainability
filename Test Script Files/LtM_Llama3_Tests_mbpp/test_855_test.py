import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):
    def test_even_parity(self):
        self.assertTrue(check_Even_Parity(0))
        self.assertTrue(check_Even_Parity(2))
        self.assertTrue(check_Even_Parity(4))
        self.assertTrue(check_Even_Parity(6))
        self.assertFalse(check_Even_Parity(1))
        self.assertFalse(check_Even_Parity(3))
        self.assertFalse(check_Even_Parity(5))
        self.assertFalse(check_Even_Parity(7))

    def test_edge_cases(self):
        self.assertFalse(check_Even_Parity(1))
        self.assertFalse(check_Even_Parity(3))
        self.assertFalse(check_Even_Parity(5))
        self.assertFalse(check_Even_Parity(7))
        self.assertTrue(check_Even_Parity(8))
        self.assertTrue(check_Even_Parity(10))
        self.assertTrue(check_Even_Parity(12))
        self.assertTrue(check_Even_Parity(14))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_Even_Parity('a')
        with self.assertRaises(TypeError):
            check_Even_Parity(None)
        with self.assertRaises(TypeError):
            check_Even_Parity(1.5)
