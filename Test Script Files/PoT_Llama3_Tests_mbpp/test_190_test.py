import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Intgral_Points(1, 1, 3, 3), 4)

    def test_edge_case_x1_x2_equal(self):
        self.assertEqual(count_Intgral_Points(1, 1, 1, 3), 2)

    def test_edge_case_y1_y2_equal(self):
        self.assertEqual(count_Intgral_Points(1, 1, 3, 1), 2)

    def test_edge_case_x1_x2_y1_y2_equal(self):
        self.assertEqual(count_Intgral_Points(1, 1, 1, 1), 0)

    def test_edge_case_x1_x2_y1_y2_negative(self):
        self.assertEqual(count_Intgral_Points(-1, -1, -3, -3), 4)

    def test_edge_case_x1_x2_y1_y2_zero(self):
        self.assertEqual(count_Intgral_Points(0, 0, 0, 0), 0)

    def test_edge_case_x1_x2_y1_y2_negative_zero(self):
        self.assertEqual(count_Intgral_Points(-1, 0, 0, -3), 3)
