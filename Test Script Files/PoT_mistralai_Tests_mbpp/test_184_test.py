import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4], 1))
        self.assertTrue(greater_specificnum([-1, -2, -3, -4], -5))
        self.assertTrue(greater_specificnum([0, 1, 2, 3], 0))

    def test_edge_case(self):
        self.assertFalse(greater_specificnum([0, 0, 0, 0], 1))
        self.assertFalse(greater_specificnum([-1, 0, 1], -2))
        self.assertFalse(greater_specificnum([1, 2, 3], 4))

    def test_boundary_case(self):
        self.assertTrue(greater_specificnum([-1], -1))
        self.assertTrue(greater_specificnum([0], 0))
        self.assertTrue(greater_specificnum([1], 1))
