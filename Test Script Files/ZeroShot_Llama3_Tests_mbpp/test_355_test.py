import unittest
from mbpp_355_code import count_Rectangles

class TestCount_Rectangles(unittest.TestCase):

    def test_count_Rectangles(self):
        self.assertEqual(count_Rectangles(0), 0)
        self.assertEqual(count_Rectangles(1), 1)
        self.assertEqual(count_Rectangles(2), 5)
        self.assertEqual(count_Rectangles(3), 13)
        self.assertEqual(count_Rectangles(4), 25)
        self.assertEqual(count_Rectangles(5), 41)
        self.assertEqual(count_Rectangles(6), 61)
        self.assertEqual(count_Rectangles(7), 85)
        self.assertEqual(count_Rectangles(8), 113)
        self.assertEqual(count_Rectangles(9), 145)
        self.assertEqual(count_Rectangles(10), 181)
