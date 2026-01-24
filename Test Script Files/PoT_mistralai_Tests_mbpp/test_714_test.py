import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Fac(1), 1)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 2)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(6), 1)
        self.assertEqual(count_Fac(7), 2)
        self.assertEqual(count_Fac(8), 2)
        self.assertEqual(count_Fac(9), 1)
        self.assertEqual(count_Fac(10), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(100), 24)
        self.assertEqual(count_Fac(120), 12)
        self.assertEqual(count_Fac(121), 11)
        self.assertEqual(count_Fac(200), 41)
        self.assertEqual(count_Fac(201), 40)
        self.assertEqual(count_Fac(1000), 164)
