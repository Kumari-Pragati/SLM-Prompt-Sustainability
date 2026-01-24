import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Intgral_Points(1, 1, 3, 3), 4)

    def test_edge_cases(self):
        self.assertEqual(count_Intgral_Points(1, 1, 2, 2), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 1, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_Intgral_Points(1, 1, 2, 3), 1)
        self.assertEqual(count_Intgral_Points(1, 1, 3, 2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Intgral_Points('1', 1, 3, 3)
        with self.assertRaises(TypeError):
            count_Intgral_Points(1, '1', 3, 3)
        with self.assertRaises(TypeError):
            count_Intgral_Points(1, 1, '3', 3)
        with self.assertRaises(TypeError):
            count_Intgral_Points(1, 1, 3, '3')
