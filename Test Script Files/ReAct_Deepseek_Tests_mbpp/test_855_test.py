import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_Even_Parity(10))
        self.assertFalse(check_Even_Parity(7))
        self.assertTrue(check_Even_Parity(18))
        self.assertFalse(check_Even_Parity(21))

    def test_boundary_cases(self):
        self.assertTrue(check_Even_Parity(0))
        self.assertFalse(check_Even_Parity(1))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            check_Even_Parity("10")
        with self.assertRaises(TypeError):
            check_Even_Parity(None)
