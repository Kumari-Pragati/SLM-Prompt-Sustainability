import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (-1, -1))

    def test_same_left_right_values(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))

    def test_different_left_right_values(self):
        self.assertEqual(find_Points(1, 2, 3, 2), (1, 2))

    def test_same_left_value_different_right_value(self):
        self.assertEqual(find_Points(1, 2, 1, 3), (1, 3))

    def test_same_right_value_different_left_value(self):
        self.assertEqual(find_Points(2, 2, 1, 2), (2, 2))

    def test_negative_values(self):
        self.assertEqual(find_Points(-1, -2, -3, -4), (-1, -1))

    def test_zero_values(self):
        self.assertEqual(find_Points(0, 2, 0, 4), (0, 4))
