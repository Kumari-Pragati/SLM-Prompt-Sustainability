import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Intgral_Points(1, 1, 3, 3), 4)

    def test_edge_case_same_coordinates(self):
        self.assertEqual(count_Intgral_Points(1, 1, 1, 1), 0)

    def test_edge_case_one_dimensional(self):
        self.assertEqual(count_Intgral_Points(1, 1, 2, 1), 0)

    def test_negative_coordinates(self):
        self.assertEqual(count_Intgral_Points(-1, -1, 1, 1), 4)

    def test_zero_coordinates(self):
        self.assertEqual(count_Intgral_Points(0, 0, 2, 2), 4)

    def test_large_coordinates(self):
        self.assertEqual(count_Intgral_Points(100, 100, 200, 200), 80100)
