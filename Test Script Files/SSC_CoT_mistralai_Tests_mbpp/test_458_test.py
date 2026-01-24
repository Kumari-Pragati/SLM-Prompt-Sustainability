import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(rectangle_area(3, 4), 12)

    def test_edge_input(self):
        self.assertEqual(rectangle_area(0, 4), 0)
        self.assertEqual(rectangle_area(4, 0), 0)
        self.assertEqual(rectangle_area(1, 1), 1)

    def test_negative_input(self):
        self.assertEqual(rectangle_area(-3, 4), None)
        self.assertEqual(rectangle_area(3, -4), None)

    def test_float_input(self):
        self.assertAlmostEqual(rectangle_area(3.5, 4.5), 15.75)
