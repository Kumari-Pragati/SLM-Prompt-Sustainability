import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_simple_positive_area(self):
        self.assertEqual(triangle_area(5), 25)

    def test_zero_area(self):
        self.assertEqual(triangle_area(0), 0)

    def test_negative_input(self):
        self.assertEqual(triangle_area(-1), -1)

    def test_large_number_area(self):
        self.assertEqual(triangle_area(10000), 100000000)

    def test_float_input(self):
        self.assertAlmostEqual(triangle_area(3.5), 12.25)

    def test_negative_area(self):
        self.assertEqual(triangle_area(-5), -1)
