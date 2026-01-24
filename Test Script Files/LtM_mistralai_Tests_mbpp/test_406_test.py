import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    def test_simple_even(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_simple_odd(self):
        self.assertEqual(find_Parity(1), "Odd Parity")

    def test_edge_min(self):
        self.assertEqual(find_Parity(2**31), "Even Parity")

    def test_edge_max(self):
        self.assertEqual(find_Parity(2**32 - 1), "Odd Parity")

    def test_edge_negative(self):
        self.assertEqual(find_Parity(-1), "Odd Parity")

    def test_edge_zero(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_combined(self):
        self.assertEqual(find_Parity(2**15 + 1), "Odd Parity")
