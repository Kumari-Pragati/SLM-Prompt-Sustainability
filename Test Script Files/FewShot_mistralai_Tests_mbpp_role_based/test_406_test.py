import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    def test_even_parity(self):
        self.assertEqual(find_Parity(0), "Even Parity")
        self.assertEqual(find_Parity(2), "Even Parity")
        self.assertEqual(find_Parity(4), "Even Parity")
        self.assertEqual(find_Parity(6), "Even Parity")

    def test_odd_parity(self):
        self.assertEqual(find_Parity(1), "Odd Parity")
        self.assertEqual(find_Parity(3), "Odd Parity")
        self.assertEqual(find_Parity(5), "Odd Parity")
        self.assertEqual(find_Parity(7), "Odd Parity")

    def test_zero(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_negative_numbers(self):
        self.assertEqual(find_Parity(-1), "Odd Parity")
        self.assertEqual(find_Parity(-3), "Odd Parity")
        self.assertEqual(find_Parity(-5), "Odd Parity")
        self.assertEqual(find_Parity(-7), "Odd Parity")

    def test_max_int(self):
        self.assertEqual(find_Parity(2**31 - 1), "Odd Parity")

    def test_min_int(self):
        self.assertEqual(find_Parity(-2**31), "Odd Parity")
