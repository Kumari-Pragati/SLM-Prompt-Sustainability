import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 2))

    def test_edge_case(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 6))

    def test_boundary_case(self):
        self.assertTrue(greater_specificnum([10, 20, 30, 40, 50], 10))
        self.assertFalse(greater_specificnum([10, 20, 30, 40, 50], 60))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            greater_specificnum("1, 2, 3, 4, 5", 2)
        with self.assertRaises(TypeError):
            greater_specificnum([1, 2, 3, 4, "5"], 2)
