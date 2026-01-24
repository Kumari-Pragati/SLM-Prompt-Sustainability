import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_odd(1))
        self.assertFalse(is_odd(2))
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(4))

    def test_edge_cases(self):
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(-2))
        self.assertTrue(is_odd(-1))

    def test_boundary_cases(self):
        self.assertTrue(is_odd(2**63 - 1))
        self.assertFalse(is_odd(2**63))
