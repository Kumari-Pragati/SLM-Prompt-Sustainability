import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):

    def test_simple_even(self):
        self.assertTrue(check_Even_Parity(2))
        self.assertTrue(check_Even_Parity(4))
        self.assertTrue(check_Even_Parity(6))

    def test_simple_odd(self):
        self.assertFalse(check_Even_Parity(1))
        self.assertFalse(check_Even_Parity(3))
        self.assertFalse(check_Even_Parity(5))

    def test_edge_cases(self):
        self.assertTrue(check_Even_Parity(0))
        self.assertTrue(check_Even_Parity(2147483646))  # max int
        self.assertFalse(check_Even_Parity(-1))  # min int
        self.assertFalse(check_Even_Parity(-2147483647))  # max int neg

    def test_complex_cases(self):
        self.assertTrue(check_Even_Parity(1024))  # power of 2
        self.assertFalse(check_Even_Parity(1025))  # power of 2 + 1
        self.assertTrue(check_Even_Parity(10241024))  # power of 2 * power of 2
        self.assertFalse(check_Even_Parity(10241025))  # power of 2 * power of 2 + 1
