import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Rectangles(1), 5)
        self.assertEqual(count_Rectangles(2), 25)
        self.assertEqual(count_rectangles(3), 41)

    def test_edge_cases(self):
        self.assertEqual(count_Rectangles(0), 0)
        self.assertEqual(count_Rectangles(1), 5)
        self.assertEqual(count_Rectangles(2), 25)
        self.assertEqual(count_Rectangles(3), 41)
        self.assertEqual(count_Rectangles(4), 61)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            count_Rectangles('radius')
        with self.assertRaises(ValueError):
            count_Rectangles(-1)
