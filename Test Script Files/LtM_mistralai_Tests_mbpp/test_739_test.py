import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(find_Index(1), 4)
        self.assertEqual(find_Index(2), 10)
        self.assertEqual(find_Index(3), 22)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Index(0), 0)
        self.assertEqual(find_Index(math.isinf()), math.isinf())

    def test_complex_input(self):
        self.assertEqual(find_Index(math.isnan()), math.nan)
        self.assertEqual(find_Index(math.inf), math.inf)
        self.assertEqual(find_Index(-1), -1)
