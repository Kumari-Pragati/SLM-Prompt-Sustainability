import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_zero_radius(self):
        self.assertEqual(count_Rectangles(0), 0)

    def test_one_radius(self):
        self.assertEqual(count_Rectangles(1), 1)

    def test_two_radius(self):
        self.assertEqual(count_Rectangles(2), 5)

    def test_three_radius(self):
        self.assertEqual(count_Rectangles(3), 13)

    def test_large_radius(self):
        self.assertEqual(count_Rectangles(10), 385)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            count_Rectangles(-1)

    def test_non_integer_radius(self):
        with self.assertRaises(TypeError):
            count_Rectangles(3.5)
