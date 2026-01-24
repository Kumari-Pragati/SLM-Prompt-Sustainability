import unittest
from mbpp_355_code import count_Rectangles

class TestCount_Rectangles(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(count_Rectangles(0), 0)

    def test_small_radius(self):
        self.assertEqual(count_Rectangles(1), 1)

    def test_medium_radius(self):
        self.assertEqual(count_Rectangles(5), 21)

    def test_large_radius(self):
        self.assertEqual(count_Rectangles(10), 385)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            count_Rectangles(-1)
