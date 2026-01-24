import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(count_Rectangles(1), 0)
        self.assertEqual(count_Rectangles(2), 1)
        self.assertEqual(count_Rectangles(3), 3)
        self.assertEqual(count_Rectangles(4), 6)
        self.assertEqual(count_Rectangles(5), 10)

    def test_zero(self):
        self.assertEqual(count_Rectangles(0), 0)

    def test_negative_integer(self):
        self.assertEqual(count_Rectangles(-1), 0)

    def test_float(self):
        self.assertEqual(count_Rectangles(2.5), 1)

    def test_large_integer(self):
        self.assertEqual(count_Rectangles(1000), 3318300)
