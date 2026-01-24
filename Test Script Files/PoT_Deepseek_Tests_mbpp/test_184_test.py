import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(greater_specificnum([10, 20, 30], 5))
        self.assertFalse(greater_specificnum([10, 20, 30], 30))

    def test_edge_cases(self):
        self.assertTrue(greater_specificnum([], 0))
        self.assertFalse(greater_specificnum([10, 20, 30], 40))

    def test_boundary_conditions(self):
        self.assertTrue(greater_specificnum([10, 20, 30], 30))
        self.assertFalse(greater_specificnum([10, 20, 30], 40))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            greater_specificnum("not a list", 10)
        with self.assertRaises(TypeError):
            greater_specificnum([10, 20, "not a number"], 10)
