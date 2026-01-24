import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Rectangles(1), 5)
        self.assertEqual(count_Rectangles(2), 25)

    def test_boundary_conditions(self):
        self.assertEqual(count_Rectangles(0), 0)
        self.assertEqual(count_Rectangles(10), 3925)

    def test_edge_cases(self):
        self.assertEqual(count_Rectangles(100), 80401)
        self.assertEqual(count_Rectangles(1000), 8004001)
