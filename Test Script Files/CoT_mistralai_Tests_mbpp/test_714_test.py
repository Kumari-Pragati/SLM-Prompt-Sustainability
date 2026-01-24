import unittest
from714_code import count_Fac

class TestCountFac(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Fac(1), 1)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 1)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(6), 1)
        self.assertEqual(count_Fac(10), 4)
        self.assertEqual(count_Fac(12), 6)
        self.assertEqual(count_Fac(24), 8)

    def test_edge_case(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(1024), 168)
        self.assertEqual(count_Fac(1025), 1)
        self.assertEqual(count_Fac(2147483647), 1)

    def test_boundary_case(self):
        self.assertEqual(count_Fac(-1), None)
        self.assertEqual(count_Fac(1.5), None)
        self.assertEqual(count_Fac(float('inf')), None)
        self.assertEqual(count_Fac(complex(0, 1)), None)
