import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    def test_even_parity(self):
        self.assertEqual(find_Parity(0), "Even Parity")
        self.assertEqual(find_Parity(2), "Even Parity")
        self.assertEqual(find_Parity(4), "Even Parity")
        self.assertEqual(find_Parity(6), "Even Parity")
        self.assertEqual(find_Parity(8), "Even Parity")

    def test_odd_parity(self):
        self.assertEqual(find_Parity(1), "Odd Parity")
        self.assertEqual(find_Parity(3), "Odd Parity")
        self.assertEqual(find_Parity(5), "Odd Parity")
        self.assertEqual(find_Parity(7), "Odd Parity")
        self.assertEqual(find_Parity(9), "Odd Parity")

    def test_edge_cases(self):
        self.assertEqual(find_Parity(0x7FFF), "Odd Parity")
        self.assertEqual(find_Parity(0x8000), "Even Parity")
        self.assertEqual(find_Parity(0xFFFF), "Odd Parity")
        self.assertEqual(find_Parity(0x10000), "Even Parity")
        self.assertEqual(find_Parity(0xFFFFFFFF), "Odd Parity")
