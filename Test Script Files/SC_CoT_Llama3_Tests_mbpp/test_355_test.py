import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_Rectangles(5), 21)

    def test_edge_case_zero_radius(self):
        self.assertEqual(count_Rectangles(0), 1)

    def test_edge_case_one_radius(self):
        self.assertEqual(count_Rectangles(1), 1)

    def test_edge_case_two_radius(self):
        self.assertEqual(count_Rectangles(2), 5)

    def test_edge_case_large_radius(self):
        self.assertEqual(count_Rectangles(10), 385)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            count_Rectangles('a')

    def test_invalid_input_negative_radius(self):
        with self.assertRaises(TypeError):
            count_Rectangles(-1)

    def test_invalid_input_zero_radius(self):
        with self.assertRaises(TypeError):
            count_Rectangles(0)
