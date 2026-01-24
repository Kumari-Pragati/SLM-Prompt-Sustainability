import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Index(1), 3)
        self.assertEqual(find_Index(2), 14)
        self.assertEqual(find_Index(3), 45)

    def test_edge_conditions(self):
        self.assertEqual(find_Index(0), 2)
        self.assertEqual(find_Index(-1), 2)

    def test_boundary_conditions(self):
        self.assertEqual(find_Index(4), 100)
        self.assertEqual(find_Index(5), 199)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Index('a')
        with self.assertRaises(ValueError):
            find_Index(-2)
