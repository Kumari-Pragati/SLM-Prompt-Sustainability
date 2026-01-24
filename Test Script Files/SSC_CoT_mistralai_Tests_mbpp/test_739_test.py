import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(find_Index(1), 1)
        self.assertEqual(find_Index(2), 2)
        self.assertEqual(find_Index(10), 4.47213595499958)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Index(0), 0)
        self.assertEqual(find_Index(1000), 21.9722457734621)
        self.assertAlmostEqual(find_Index(-1), -1)

    def test_invalid_input(self):
        self.assertRaises(ValueError, find_Index, -2)
        self.assertRaises(ValueError, find_Index, float('inf'))
        self.assertRaises(ValueError, find_Index, complex(0, 1))
