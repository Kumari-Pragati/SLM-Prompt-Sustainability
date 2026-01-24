import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(10), 3)
        self.assertEqual(count_Fac(20), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(100), 10)
        self.assertEqual(count_Fac(1000), 11)

    def test_corner_cases(self):
        self.assertEqual(count_Fac(714), 10)
        self.assertEqual(count_Fac(10000), 12)
        self.assertEqual(count_Fac(100000), 13)
