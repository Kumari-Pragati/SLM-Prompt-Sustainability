import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Intgral_Points(1, 1, 5, 5), 12)

    def test_edge_case_same_coordinates(self):
        self.assertEqual(count_Intgral_Points(1, 1, 1, 1), 0)

    def test_boundary_case_one_coordinate(self):
        self.assertEqual(count_Intgral_Points(1, 1, 1, 5), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 5, 1), 0)

    def test_boundary_case_two_coordinates(self):
        self.assertEqual(count_Intgral_Points(1, 1, 2, 2), 0)

    def test_corner_case_negative_coordinates(self):
        self.assertEqual(count_Intgral_Points(-1, -1, 1, 1), 4)

    def test_corner_case_zero_coordinates(self):
        self.assertEqual(count_Intgral_Points(0, 0, 2, 2), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Intgral_Points("1", 1, 5, 5)
