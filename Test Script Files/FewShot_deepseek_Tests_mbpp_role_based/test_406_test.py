import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Parity(7), "Odd Parity")
        self.assertEqual(find_Parity(10), "Even Parity")

    def test_boundary_conditions(self):
        self.assertEqual(find_Parity(0), "Even Parity")
        self.assertEqual(find_Parity(1), "Odd Parity")

    def test_edge_cases(self):
        self.assertEqual(find_Parity(2**31 - 1), "Odd Parity")
        self.assertEqual(find_Parity(2**31), "Even Parity")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Parity("invalid")
