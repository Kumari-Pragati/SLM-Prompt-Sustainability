import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Index(1), 2)
        self.assertEqual(find_Index(2), 4)
        self.assertEqual(find_Index(3), 6)
        self.assertEqual(find_Index(4), 8)
        self.assertEqual(find_Index(5), 10)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_Index(0), 0)
        self.assertEqual(find_Index(1000), 1000 * math.sqrt(2))
        self.assertEqual(find_Index(-1), -1)
        self.assertEqual(find_Index(float('inf')), float('inf'))
        self.assertEqual(find_Index(complex(0, 0)), 0)
