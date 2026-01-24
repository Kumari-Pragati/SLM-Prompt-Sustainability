import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_Odd_Parity(7))  # Odd number with 1 set bit
        self.assertFalse(check_Odd_Parity(4))  # Even number with 0 set bits
        self.assertTrue(check_Odd_Parity(15))  # Odd number with 3 set bits
        self.assertFalse(check_Odd_Parity(0))  # Zero

    def test_edge_cases(self):
        self.assertTrue(check_Odd_Parity(1))  # Single set bit
        self.assertFalse(check_Odd_Parity(2))  # Even number with 1 set bit
        self.assertTrue(check_Odd_Parity(3))  # Odd number with 2 set bits
        self.assertFalse(check_Odd_Parity(1024))  # Large even number

    def test_explicitly_handled_error_cases(self):
        # Negative numbers should be handled gracefully
        self.assertFalse(check_Odd_Parity(-7))
        self.assertFalse(check_Odd_Parity(-15))
        # Non-integer inputs should raise a TypeError
        with self.assertRaises(TypeError):
            check_Odd_Parity("7")
        with self.assertRaises(TypeError):
            check_Odd_Parity(7.5)
