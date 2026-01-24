import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_Rectangles(1), 1)
        self.assertEqual(count_Rectangles(2), 3)
        self.assertEqual(count_Rectangles(3), 6)
        self.assertEqual(count_Rectangles(4), 10)
        self.assertEqual(count_Rectangles(5), 15)

    def test_edge_input(self):
        self.assertEqual(count_Rectangles(0), 0)
        self.assertEqual(count_Rectangles(100), 3125)

    def test_boundary_input(self):
        self.assertEqual(count_Rectangles(1.5), 3)
        self.assertEqual(count_Rectangles(2.5), 15)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_Rectangles, 'a_string')
        self.assertRaises(TypeError, count_Rectangles, -1)
        self.assertRaises(TypeError, count_Rectangles, 0.0)
