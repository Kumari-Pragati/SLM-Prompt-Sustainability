import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    def test_even_parity(self):
        self.assertEqual(find_Parity(0), "Even Parity")
        self.assertEqual(find_Parity(2), "Even Parity")
        self.assertEqual(find_Parity(4), "Even Parity")
        self.assertEqual(find_Parity(6), "Even Parity")
        self.assertEqual(find_Parity(8), "Even Parity")
        self.assertEqual(find_Parity(10), "Even Parity")
        self.assertEqual(find_Parity(14), "Even Parity")
        self.assertEqual(find_Parity(16), "Even Parity")
        self.assertEqual(find_Parity(30), "Even Parity")
        self.assertEqual(find_Parity(32), "Even Parity")

    def test_odd_parity(self):
        self.assertEqual(find_Parity(1), "Odd Parity")
        self.assertEqual(find_Parity(3), "Odd Parity")
        self.assertEqual(find_Parity(5), "Odd Parity")
        self.assertEqual(find_Parity(7), "Odd Parity")
        self.assertEqual(find_Parity(9), "Odd Parity")
        self.assertEqual(find_Parity(11), "Odd Parity")
        self.assertEqual(find_Parity(13), "Odd Parity")
        self.assertEqual(find_Parity(15), "Odd Parity")
        self.assertEqual(find_Parity(29), "Odd Parity")
        self.assertEqual(find_Parity(31), "Odd Parity")

    def test_edge_cases(self):
        self.assertEqual(find_Parity(-1), "Odd Parity")
        self.assertEqual(find_Parity(-3), "Odd Parity")
        self.assertEqual(find_Parity(-5), "Odd Parity")
        self.assertEqual(find_Parity(-7), "Odd Parity")
        self.assertEqual(find_Parity(-9), "Odd Parity")
        self.assertEqual(find_Parity(-11), "Odd Parity")
        self.assertEqual(find_Parity(-13), "Odd Parity")
        self.assertEqual(find_Parity(-15), "Odd Parity")
        self.assertEqual(find_Parity(-29), "Odd Parity")
        self.assertEqual(find_Parity(-31), "Odd Parity")

        self.assertEqual(find_Parity(2**31 - 1), "Odd Parity")
        self.assertEqual(find_Parity(2**31), "Odd Parity")
        self.assertEqual(find_Parity(2**32 - 1), "Odd Parity")

        self.assertEqual(find_Parity(0b1), "Odd Parity")
        self.assertEqual(find_Parity(0b10), "Even Parity")
        self.assertEqual(find_Parity(0b100), "Odd Parity")
        self.assertEqual(find_Parity(0b1000), "Even Parity")
        self.assertEqual(find_Parity(0b10000), "Odd Parity")
        self.assertEqual(find_Parity(0b1000000), "Even Parity")
