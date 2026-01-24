import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):

    def test_even_parity_typical_case(self):
        self.assertEqual(find_Parity(0), "Even Parity")
        self.assertEqual(find_Parity(1), "Odd Parity")
        self.assertEqual(find_Parity(2), "Even Parity")
        self.assertEqual(find_Parity(3), "Odd Parity")

    def test_even_parity_edge_cases(self):
        self.assertEqual(find_Parity(2**31), "Even Parity")
        self.assertEqual(find_Parity(2**32 - 1), "Odd Parity")

    def test_odd_parity_typical_case(self):
        self.assertEqual(find_Parity(2**31 + 1), "Odd Parity")
        self.assertEqual(find_Parity(2**32), "Even Parity")

    def test_odd_parity_edge_cases(self):
        self.assertEqual(find_Parity(2**63 - 1), "Odd Parity")
        self.assertEqual(find_Parity(2**63), "Even Parity")

    def test_negative_numbers(self):
        self.assertEqual(find_Parity(-1), "Odd Parity")
        self.assertEqual(find_Parity(-2), "Even Parity")

    def test_large_numbers(self):
        self.assertEqual(find_Parity(10**18), "Even Parity")
        self.assertEqual(find_Parity(10**18 + 1), "Odd Parity")
