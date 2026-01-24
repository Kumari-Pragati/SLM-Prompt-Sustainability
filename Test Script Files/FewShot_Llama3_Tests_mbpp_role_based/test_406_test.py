import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(find_Parity(4), "Even Parity")

    def test_odd_number(self):
        self.assertEqual(find_Parity(5), "Odd Parity")

    def test_zero(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_negative_number(self):
        self.assertEqual(find_Parity(-4), "Even Parity")

    def test_large_number(self):
        self.assertEqual(find_Parity(1000), "Even Parity")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_Parity("hello")
