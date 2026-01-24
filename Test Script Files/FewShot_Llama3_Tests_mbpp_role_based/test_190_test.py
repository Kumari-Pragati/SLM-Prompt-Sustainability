import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Intgral_Points(1, 2, 3, 4), 8)

    def test_edge_case_x1_x2_equal(self):
        self.assertEqual(count_Intgral_Points(1, 2, 1, 2), 0)

    def test_edge_case_y1_y2_equal(self):
        self.assertEqual(count_Intgral_Points(1, 1, 2, 1), 0)

    def test_edge_case_x1_x2_y1_y2_equal(self):
        self.assertEqual(count_Intgral_Points(1, 1, 1, 1), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_Intgral_Points('a', 2, 3, 4)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            count_Intgral_Points(1, 2, 'a', 4)
