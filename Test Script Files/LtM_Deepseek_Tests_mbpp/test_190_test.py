import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_Intgral_Points(1, 1, 3, 3), 4)

    def test_edge_conditions(self):
        self.assertEqual(count_Intgral_Points(1, 1, 1, 1), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 2, 2), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 1, 2), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 2, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_Intgral_Points(1, 1, 2, 3), 1)
        self.assertEqual(count_Intgral_Points(1, 1, 3, 2), 1)

    def test_complex_cases(self):
        self.assertEqual(count_Intgral_Points(-1, -1, 1, 1), 4)
        self.assertEqual(count_Intgral_Points(-1, -1, 0, 0), 1)
        self.assertEqual(count_Intgral_Points(0, 0, 1, 1), 1)
