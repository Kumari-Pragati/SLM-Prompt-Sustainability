import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(find_Index(1), 3)
        self.assertEqual(find_Index(2), 10)
        self.assertEqual(find_Index(3), 32)
        self.assertEqual(find_Index(4), 100)

    def test_boundary_conditions(self):
        self.assertEqual(find_Index(0), 3)
        self.assertEqual(find_Index(-1), 3)

    def test_edge_cases(self):
        self.assertEqual(find_Index(1000), 547558437)
        self.assertEqual(find_Index(1001), 547558437)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Index('a')
        with self.assertRaises(ValueError):
            find_Index(-2)
