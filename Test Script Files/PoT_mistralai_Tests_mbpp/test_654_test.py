import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rectangle_perimeter(3, 4), 14)

    def test_edge_case_zero(self):
        self.assertEqual(rectangle_perimeter(0, 4), 8)
        self.assertEqual(rectangle_perimeter(4, 0), 8)

    def test_edge_case_one(self):
        self.assertEqual(rectangle_perimeter(1, 4), 10)
        self.assertEqual(rectangle_perimeter(4, 1), 10)

    def test_boundary_case_negative(self):
        self.assertEqual(rectangle_perimeter(-3, 4), 14)
        self.assertEqual(rectangle_perimeter(3, -4), 14)
