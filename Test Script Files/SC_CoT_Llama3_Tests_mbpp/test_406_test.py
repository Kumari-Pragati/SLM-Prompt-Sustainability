import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):

    def test_even_parity(self):
        self.assertEqual(find_Parity(10), "Even Parity")

    def test_odd_parity(self):
        self.assertEqual(find_Parity(11), "Odd Parity")

    def test_edge_case_zero(self):
        self.assertEqual(find_Parity(0), "Even Parity")

    def test_edge_case_negative(self):
        self.assertEqual(find_Parity(-10), "Even Parity")

    def test_edge_case_max_int(self):
        self.assertEqual(find_Parity(2**31 - 1), "Odd Parity")

    def test_edge_case_max_int_plus_one(self):
        self.assertEqual(find_Parity(2**31), "Even Parity")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            find_Parity("hello")

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            find_Parity([1, 2, 3])
