import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):

    def test_find_parity_zero(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_find_parity_one(self):
        self.assertEqual(find_Parity(1), "Odd Parity")

    def test_find_parity_negative_one(self):
        self.assertEqual(find_Parity(-1), "Odd Parity")

    def test_find_parity_two(self):
        self.assertEqual(find_Parity(2), "Even Parity")

    def test_find_parity_four(self):
        self.assertEqual(find_Parity(4), "Even Parity")

    def test_find_parity_five(self):
        self.assertEqual(find_Parity(5), "Odd Parity")

    def test_find_parity_max_int(self):
        self.assertEqual(find_Parity(2147483647), "Odd Parity")

    def test_find_parity_min_int(self):
        self.assertEqual(find_Parity(-2147483648), "Even Parity")

    def test_find_parity_large_number(self):
        self.assertEqual(find_Parity(1234567890123456789), "Odd Parity")
