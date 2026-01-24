import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_rectangle_area_typical(self):
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(5, 0), 0)

    def test_rectangle_area_edge(self):
        self.assertEqual(rectangle_area(1, 1), 1)
        self.assertEqual(rectangle_area(-3, 4), 12)
        self.assertEqual(rectangle_area(3, -4), 12)
