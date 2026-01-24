import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):

    def test_even_parity(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_odd_parity(self):
        self.assertEqual(find_Parity(1), "Odd Parity")

    def test_even_parity_with_large_number(self):
        self.assertEqual(find_Parity(2**16 - 1), "Even Parity")

    def test_odd_parity_with_large_number(self):
        self.assertEqual(find_Parity(2**16), "Odd Parity")

    def test_edge_case(self):
        self.assertEqual(find_Parity(2**31 - 1), "Even Parity")

    def test_edge_case_with_negative_number(self):
        self.assertEqual(find_Parity(-1), "Odd Parity")
