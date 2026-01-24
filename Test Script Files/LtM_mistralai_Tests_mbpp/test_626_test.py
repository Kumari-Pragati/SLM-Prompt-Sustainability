import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(triangle_area(2), 4)

    def test_edge_zero(self):
        self.assertEqual(triangle_area(0), 0)

    def test_edge_negative(self):
        self.assertEqual(triangle_area(-1), -1)

    def test_large_input(self):
        self.assertEqual(triangle_area(1000), 1000000)
