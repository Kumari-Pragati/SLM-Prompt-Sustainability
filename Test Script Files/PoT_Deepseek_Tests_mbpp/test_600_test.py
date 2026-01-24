import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Even(2))
        self.assertTrue(is_Even(0))
        self.assertFalse(is_Even(1))

    def test_edge_cases(self):
        self.assertFalse(is_Even(-1))
        self.assertTrue(is_Even(-2))

    def test_boundary_cases(self):
        self.assertFalse(is_Even(2**63 - 1))
        self.assertTrue(is_Even(2**63))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Even(None)
        with self.assertRaises(TypeError):
            is_Even('string')
        with self.assertRaises(TypeError):
            is_Even([])
