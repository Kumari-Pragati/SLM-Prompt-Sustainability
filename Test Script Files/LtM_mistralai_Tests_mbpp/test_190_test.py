import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntgralPoints(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_Intgral_Points(1, 1, 2, 2), 1)
        self.assertEqual(count_Intgral_Points(2, 2, 3, 3), 1)
        self.assertEqual(count_Intgral_Points(0, 0, 1, 1), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(count_Intgral_Points(0, 0, 0, 1), 0)
        self.assertEqual(count_Intgral_Points(1, 1, 2, 3), 2)
        self.assertEqual(count_Intgral_Points(1, 1, 1, 2), 0)
        self.assertEqual(count_Intgral_Points(-1, -1, 0, 0), 0)

    def test_complex(self):
        self.assertEqual(count_Intgral_Points(1, 1, 3, 5), 10)
        self.assertEqual(count_Intgral_Points(-2, -3, 0, 0), 4)
        self.assertEqual(count_Intgral_Points(0, 0, 10, 10), 90)
