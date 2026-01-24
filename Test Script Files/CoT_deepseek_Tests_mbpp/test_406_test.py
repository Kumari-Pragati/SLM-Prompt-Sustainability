import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    
    def test_positive_odd(self):
        self.assertEqual(find_Parity(1), "Odd Parity")
        self.assertEqual(find_Parity(3), "Odd Parity")
        self.assertEqual(find_Parity(7), "Odd Parity")
        self.assertEqual(find_Parity(15), "Odd Parity")

    def test_positive_even(self):
        self.assertEqual(find_Parity(2), "Even Parity")
        self.assertEqual(find_Parity(4), "Even Parity")
        self.assertEqual(find_Parity(8), "Even Parity")
        self.assertEqual(find_Parity(16), "Even Parity")

    def test_negative(self):
        self.assertEqual(find_Parity(-1), "Odd Parity")
        self.assertEqual(find_Parity(-3), "Odd Parity")
        self.assertEqual(find_Parity(-7), "Odd Parity")
        self.assertEqual(find_Parity(-15), "Odd Parity")

    def test_zero(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_large_number(self):
        self.assertEqual(find_Parity(2**31 - 1), "Odd Parity")

    def test_large_negative_number(self):
        self.assertEqual(find_Parity(-2**31), "Even Parity")

    def test_large_float(self):
        self.assertEqual(find_Parity(1.5), "Odd Parity")
        self.assertEqual(find_Parity(-1.5), "Odd Parity")

    def test_string(self):
        self.assertEqual(find_Parity("1"), "Odd Parity")
        self.assertEqual(find_Parity("abc"), "Odd Parity")

    def test_list(self):
        self.assertEqual(find_Parity([1, 2, 3]), "Odd Parity")

    def test_dict(self):
        self.assertEqual(find_Parity({"a": 1, "b": 2}), "Odd Parity")

    def test_none(self):
        self.assertEqual(find_Parity(None), "Even Parity")
