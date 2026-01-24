import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(triangle_area(5), 25)

    def test_negative_input(self):
        self.assertEqual(triangle_area(-1), -1)

    def test_zero_input(self):
        self.assertEqual(triangle_area(0), 0)

    def test_large_input(self):
        self.assertEqual(triangle_area(1000), 1000000)
