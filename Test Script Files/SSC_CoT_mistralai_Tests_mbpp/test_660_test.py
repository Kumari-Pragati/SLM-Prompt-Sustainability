import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))
        self.assertEqual(find_Points(-1, 0, 1, 2), (-1, 2))
        self.assertEqual(find_Points(0, 0, 0, 0), (-1, -1))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Points(0, 0, -1, 0), (-1, 0))
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, 1))
        self.assertEqual(find_Points(-1, -1, 0, 0), (-1, 0))
        self.assertEqual(find_Points(0, 0, 1, 0), (-1, 0))
        self.assertEqual(find_Points(0, 0, 0, -1), (-1, -1))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_Points, 'a', 'b', 'c', 'd')
        self.assertRaises(TypeError, find_Points, 1, 2, 'c', 4)
        self.assertRaises(TypeError, find_Points, 1, 2, 3, 'd')
