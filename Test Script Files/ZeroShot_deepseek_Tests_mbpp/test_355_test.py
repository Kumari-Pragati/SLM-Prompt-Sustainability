import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_count_Rectangles_with_positive_radius(self):
        self.assertEqual(count_Rectangles(1), 5)
        self.assertEqual(count_Rectangles(2), 25)
        self.assertEqual(count_Rectangles(3), 73)

    def test_count_Rectangles_with_zero_radius(self):
        self.assertEqual(count_Rectangles(0), 0)

    def test_count_Rectangles_with_negative_radius(self):
        with self.assertRaises(Exception):
            count_Rectangles(-1)
