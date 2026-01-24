import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntegralPoints(unittest.TestCase):

    def test_count_Intgral_Points(self):
        self.assertEqual(count_Intgral_Points(0,0,1,1), 0)
        self.assertEqual(count_Intgral_Points(0,0,1,2), 1)
        self.assertEqual(count_Intgral_Points(0,0,1,3), 3)
        self.assertEqual(count_Intgral_Points(0,0,1,4), 4)
        self.assertEqual(count_Intgral_Points(0,0,2,2), 3)
        self.assertEqual(count_Intgral_Points(0,0,2,3), 4)
        self.assertEqual(count_Intgral_Points(0,0,2,4), 5)
        self.assertEqual(count_Intgral_Points(0,0,3,3), 8)
        self.assertEqual(count_Intgral_Points(0,0,3,4), 9)
        self.assertEqual(count_Intgral_Points(0,0,4,4), 9)

    def test_count_Intgral_Points_edge_cases(self):
        self.assertEqual(count_Intgral_Points(0,0,0,0), 0)
        self.assertEqual(count_Intgral_Points(0,0,0,1), 0)
        self.assertEqual(count_Intgral_Points(0,0,0,2), 0)
        self.assertEqual(count_Intgral_Points(0,0,0,3), 0)
        self.assertEqual(count_Intgral_Points(0,0,0,4), 0)
        self.assertEqual(count_Intgral_Points(0,0,1,1), 0)
        self.assertEqual(count_Intgral_Points(0,0,1,2), 1)
        self.assertEqual(count_Intgral_Points(0,0,1,3), 2)
        self.assertEqual(count_Intgral_Points(0,0,1,4), 3)
        self.assertEqual(count_Intgral_Points(0,0,2,2), 1)
        self.assertEqual(count_Intgral_Points(0,0,2,3), 2)
        self.assertEqual(count_Intgral_Points(0,0,2,4), 3)
        self.assertEqual(count_Intgral_Points(0,0,3,3), 1)
        self.assertEqual(count_Intgral_Points(0,0,3,4), 2)
        self.assertEqual(count_Intgral_Points(0,0,4,4), 1)
