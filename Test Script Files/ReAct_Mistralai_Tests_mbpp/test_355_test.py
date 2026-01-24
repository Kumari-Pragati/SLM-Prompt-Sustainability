import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(count_Rectangles(1), 1)
        self.assertEqual(count_Rectangles(2), 1)
        self.assertEqual(count_Rectangles(3), 3)
        self.assertEqual(count_Rectangles(4), 4)
        self.assertEqual(count_Rectangles(5), 5)

    def test_zero(self):
        self.assertEqual(count_Rectangles(0), 0)

    def test_negative_integer(self):
        self.assertEqual(count_Rectangles(-1), 0)
        self.assertEqual(count_Rectangles(-2), 0)
        self.assertEqual(count_Rectangles(-3), 0)

    def test_large_integer(self):
        self.assertEqual(count_Rectangles(1000), 333333)

    def test_float(self):
        self.assertEqual(count_Rectangles(3.5), 3)

    def test_non_number(self):
        with self.assertRaises(TypeError):
            count_Rectangles('str')
        with self.assertRaises(TypeError):
            count_Rectangles(None)
