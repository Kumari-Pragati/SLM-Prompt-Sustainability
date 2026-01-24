import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_Rectangles(3), 12)
        self.assertEqual(count_Rectangles(5), 28)
        self.assertEqual(count_Rectangles(10), 80)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Rectangles(1), 1)
        self.assertEqual(count_Rectangles(2), 3)
        self.assertEqual(count_Rectangles(4), 10)
        self.assertEqual(count_Rectangles(6), 21)
        self.assertEqual(count_Rectangles(7), 28)
        self.assertEqual(count_Rectangles(8), 36)
        self.assertEqual(count_Rectangles(9), 45)

    def test_negative_input(self):
        self.assertRaises(ValueError, count_Rectangles, -1)

    def test_zero_input(self):
        self.assertEqual(count_Rectangles(0), 0)
