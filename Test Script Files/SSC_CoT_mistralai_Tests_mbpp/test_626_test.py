import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(triangle_area(3), 9)
        self.assertEqual(triangle_area(5), 25)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(triangle_area(0), 0)
        self.assertEqual(triangle_area(1), 1)
        self.assertEqual(triangle_area(2.5), 6.25)

    def test_negative_input(self):
        self.assertEqual(triangle_area(-1), -1)
