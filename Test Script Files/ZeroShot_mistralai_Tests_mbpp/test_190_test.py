import unittest
from mbpp_190_code import count_Intgral_Points  # replace 'your_module_name' with the actual name of the module containing the function

class TestCountIntegralPoints(unittest.TestCase):

    def test_count_integral_points_with_positive_values(self):
        self.assertEqual(count_Intgral_Points(1, 2, 3, 4), 6)
        self.assertEqual(count_Intgral_Points(0, 0, 1, 1), 0)
        self.assertEqual(count_Intgral_Points(2, 3, 4, 5), 12)

    def test_count_integral_points_with_negative_values(self):
        self.assertEqual(count_Intgral_Points(-1, -2, -3, -4), 6)
        self.assertEqual(count_Intgral_Points(0, 0, -1, -1), 0)
        self.assertEqual(count_Intgral_Points(-2, -3, -4, -5), 12)

    def test_count_integral_points_with_zero_values(self):
        self.assertEqual(count_Intgral_Points(0, 0, 0, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, 1, 0), 0)
        self.assertEqual(count_Intgral_Points(0, 0, 0, 1), 0)

    def test_count_integral_points_with_edge_cases(self):
        self.assertEqual(count_Intgral_Points(1, 2, 2, 3), 0)
        self.assertEqual(count_Intgral_Points(2, 3, 3, 4), 0)
        self.assertEqual(count_Intgral_Points(3, 4, 4, 5), 0)
        self.assertEqual(count_Intgral_Points(4, 5, 5, 6), 0)
