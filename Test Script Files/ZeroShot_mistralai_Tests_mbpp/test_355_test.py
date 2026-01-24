import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_count_rectangles_with_zero_radius(self):
        self.assertEqual(count_Rectangles(0), 0)

    def test_count_rectangles_with_one_radius(self):
        self.assertEqual(count_Rectangles(1), 1)

    def test_count_rectangles_with_two_radius(self):
        self.assertEqual(count_Rectangles(2), 5)

    def test_count_rectangles_with_three_radius(self):
        self.assertEqual(count_Rectangles(3), 14)

    def test_count_rectangles_with_four_radius(self):
        self.assertEqual(count_Rectangles(4), 30)

    def test_count_rectangles_with_five_radius(self):
        self.assertEqual(count_Rectangles(5), 55)
