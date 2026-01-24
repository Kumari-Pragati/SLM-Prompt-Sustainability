import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    def test_even_parity(self):
        self.assertEqual(find_Parity(10), "Even Parity")

    def test_odd_parity(self):
        self.assertEqual(find_Parity(11), "Odd Parity")

    def test_zero_parity(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_negative_parity(self):
        self.assertEqual(find_Parity(-10), "Even Parity")

    def test_large_parity(self):
        self.assertEqual(find_Parity(1000), "Even Parity")

    def test_small_parity(self):
        self.assertEqual(find_Parity(1), "Odd Parity")

    def test_max_parity(self):
        self.assertEqual(find_Parity(2**16 - 1), "Odd Parity")

    def test_max_parity_plus_one(self):
        self.assertEqual(find_Parity(2**16), "Even Parity")
