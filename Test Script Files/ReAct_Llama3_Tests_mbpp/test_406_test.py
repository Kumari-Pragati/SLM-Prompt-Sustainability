import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):

    def test_even_parity(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_odd_parity(self):
        self.assertEqual(find_Parity(1), "Odd Parity")

    def test_even_parity_with_power_of_two(self):
        self.assertEqual(find_Parity(2**16 - 1), "Even Parity")

    def test_odd_parity_with_power_of_two(self):
        self.assertEqual(find_Parity(2**16), "Odd Parity")

    def test_edge_case_zero(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_edge_case_max_int(self):
        self.assertEqual(find_Parity(2**31 - 1), "Odd Parity")

    def test_edge_case_max_int_plus_one(self):
        self.assertEqual(find_Parity(2**31), "Odd Parity")
