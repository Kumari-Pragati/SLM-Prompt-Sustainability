import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_simple_rectangle(self):
        self.assertEqual(rectangle_perimeter(3, 4), 14)

    def test_edge_cases_zero(self):
        self.assertEqual(rectangle_perimeter(0, 4), 8)
        self.assertEqual(rectangle_perimeter(4, 0), 8)

    def test_edge_cases_min_max(self):
        self.assertEqual(rectangle_perimeter(1, 1), 4)
        self.assertEqual(rectangle_perimeter(2147483647, 2147483647), 8294901929)

    def test_complex_rectangle(self):
        self.assertEqual(rectangle_perimeter(1000000, 1000000), 4000000000)
