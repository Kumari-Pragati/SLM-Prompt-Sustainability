import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_Rectangles(1), 4)

    def test_edge_case_min(self):
        self.assertEqual(count_Rectangles(1), 4)

    def test_edge_case_max(self):
        self.assertEqual(count_Rectangles(10000), 40000)

    def test_boundary_case_even(self):
        self.assertEqual(count_Rectangles(2), 8)

    def test_boundary_case_odd(self):
        self.assertEqual(count_Rectangles(3), 12)

    def test_complex_case(self):
        self.assertEqual(count_Rectangles(5), 60)
