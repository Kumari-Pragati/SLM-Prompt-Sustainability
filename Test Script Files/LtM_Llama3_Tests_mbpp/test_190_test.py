import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_Intgral_Points(0,0,1,1), 1)
        self.assertEqual(count_Intgral_Points(1,1,2,2), 1)
        self.assertEqual(count_Intgral_Points(0,0,0,0), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Intgral_Points(-1,-1,0,0), 0)
        self.assertEqual(count_Intgral_Points(0,0,1,1), 1)
        self.assertEqual(count_Intgral_Points(1,1,2,2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Intgral_Points('a', 'b', 'c', 'd')
        with self.assertRaises(TypeError):
            count_Intgral_Points(0,0,'a', 'b')
