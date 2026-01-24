import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Rectangles(1), 4)
        self.assertEqual(count_Rectangles(2), 9)
        self.assertEqual(count_Rectangles(3), 16)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Rectangles(0), 0)
        self.assertEqual(count_Rectangles(1000), 31415926536)
        self.assertEqual(count_Rectangles(1.5), 12)
