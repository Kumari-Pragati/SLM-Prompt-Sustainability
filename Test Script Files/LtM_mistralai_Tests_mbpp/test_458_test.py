import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rectangle_area(0, 4), 0)
        self.assertEqual(rectangle_area(4, 0), 0)
        self.assertEqual(rectangle_area(1, 1), 1)
        self.assertEqual(rectangle_area(-2, 3), 6)
        self.assertEqual(rectangle_area(2, -3), 6)

    def test_complex_cases(self):
        self.assertEqual(rectangle_area(0.5, 2), 1)
        self.assertEqual(rectangle_area(1000, 1000), 1000000)
        self.assertEqual(rectangle_area(0, 0), 0)
