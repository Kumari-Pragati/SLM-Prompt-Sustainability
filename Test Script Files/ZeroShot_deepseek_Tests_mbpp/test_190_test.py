import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):

    def test_positive_coordinates(self):
        self.assertEqual(count_Intgral_Points(1, 1, 3, 3), 4)

    def test_negative_coordinates(self):
        self.assertEqual(count_Intgral_Points(-1, -1, 1, 1), 4)

    def test_zero_coordinates(self):
        self.assertEqual(count_Intgral_Points(0, 0, 2, 2), 4)

    def test_same_coordinates(self):
        self.assertEqual(count_Intgral_Points(1, 1, 1, 1), 0)

    def test_reverse_coordinates(self):
        self.assertEqual(count_Intgral_Points(3, 3, 1, 1), 0)

    def test_equal_y_coordinates(self):
        self.assertEqual(count_Intgral_Points(1, 2, 3, 2), 0)

    def test_equal_x_coordinates(self):
        self.assertEqual(count_Intgral_Points(2, 1, 2, 3), 0)
