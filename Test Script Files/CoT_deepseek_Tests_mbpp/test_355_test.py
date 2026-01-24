import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Rectangles(1), 5)

    def test_edge_case_small_radius(self):
        self.assertEqual(count_Rectangles(0), 0)

    def test_edge_case_large_radius(self):
        self.assertEqual(count_Rectangles(100), 19605)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Rectangles('radius')

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            count_Rectangles(-1)
