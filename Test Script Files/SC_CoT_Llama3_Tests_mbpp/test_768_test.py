import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):
    def test_even_numbers(self):
        self.assertFalse(check_Odd_Parity(4))
        self.assertFalse(check_Odd_Parity(10))
        self.assertFalse(check_Odd_Parity(20))

    def test_odd_numbers(self):
        self.assertTrue(check_Odd_Parity(1))
        self.assertTrue(check_Odd_Parity(3))
        self.assertTrue(check_Odd_Parity(5))

    def test_zero(self):
        self.assertFalse(check_Odd_Parity(0))

    def test_negative_numbers(self):
        self.assertFalse(check_Odd_Parity(-4))
        self.assertFalse(check_Odd_Parity(-10))
        self.assertFalse(check_Odd_Parity(-20))

    def test_large_numbers(self):
        self.assertFalse(check_Odd_Parity(1000))
        self.assertFalse(check_Odd_Parity(2000))
        self.assertFalse(check_Odd_Parity(3000))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_Odd_Parity("hello")
        with self.assertRaises(TypeError):
            check_Odd_Parity([1, 2, 3])
