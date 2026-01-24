import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_Intgral_Points(1,1,3,3), 4)
        self.assertEqual(count_Intgral_Points(1,2,3,4), 4)
        self.assertEqual(count_Intgral_Points(1,1,2,2), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Intgral_Points(1,1,1,1), 0)
        self.assertEqual(count_Intgral_Points(1,1,2,1), 1)
        self.assertEqual(count_Intgral_Points(1,1,1,2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Intgral_Points('a',1,2,3)
        with self.assertRaises(TypeError):
            count_Intgral_Points(1,'a',2,3)
        with self.assertRaises(TypeError):
            count_Intgral_Points(1,2,'a',3)
        with self.assertRaises(TypeError):
            count_Intgral_Points(1,2,3,'a')
