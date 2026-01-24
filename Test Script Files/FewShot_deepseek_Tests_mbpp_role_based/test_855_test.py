import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_Even_Parity(10))
        self.assertFalse(check_Even_Parity(7))

    def test_boundary_conditions(self):
        self.assertTrue(check_Even_Parity(0))
        self.assertFalse(check_Even_Parity(1))

    def test_edge_conditions(self):
        self.assertTrue(check_Even_Parity(2**64 - 1))
        self.assertFalse(check_Even_Parity(2**64))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_Even_Parity("invalid")
