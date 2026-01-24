import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(triangle_area(5), 25)

    def test_edge_case_zero(self):
        self.assertEqual(triangle_area(0), 0)

    def test_boundary_case_negative(self):
        self.assertEqual(triangle_area(-1), -1)

    def test_corner_case_large_number(self):
        self.assertEqual(triangle_area(10000), 100000000)
