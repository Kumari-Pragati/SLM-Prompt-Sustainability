import unittest
from mbpp_768_code import check_Odd_Parity

class TestCheckOddParity(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_Odd_Parity(7))
        self.assertFalse(check_Odd_Parity(8))

    def test_boundary_conditions(self):
        self.assertTrue(check_Odd_Parity(1))
        self.assertFalse(check_Odd_Parity(0))

    def test_edge_cases(self):
        self.assertTrue(check_Odd_Parity(3))
        self.assertFalse(check_Odd_Parity(4))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Odd_Parity('a')
