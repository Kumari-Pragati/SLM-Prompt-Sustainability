import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 0)
        self.assertEqual(count_Fac(3), 1)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 2)
        self.assertEqual(count_Fac(6), 3)
        self.assertEqual(count_Fac(7), 2)
        self.assertEqual(count_Fac(8), 3)
        self.assertEqual(count_Fac(9), 2)
        self.assertEqual(count_Fac(10), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Fac(11), 2)
        self.assertEqual(count_Fac(12), 3)
        self.assertEqual(count_Fac(13), 2)
        self.assertEqual(count_Fac(14), 3)
        self.assertEqual(count_Fac(15), 3)
        self.assertEqual(count_Fac(16), 4)
        self.assertEqual(count_Fac(17), 3)
        self.assertEqual(count_Fac(18), 4)
        self.assertEqual(count_Fac(19), 3)
        self.assertEqual(count_Fac(20), 4)

    def test_corner_cases(self):
        self.assertEqual(count_Fac(21), 3)
        self.assertEqual(count_Fac(22), 4)
        self.assertEqual(count_Fac(23), 3)
        self.assertEqual(count_Fac(24), 4)
        self.assertEqual(count_Fac(25), 3)
        self.assertEqual(count_Fac(26), 4)
        self.assertEqual(count_Fac(27), 3)
        self.assertEqual(count_Fac(28), 4)
        self.assertEqual(count_Fac(29), 3)
        self.assertEqual(count_Fac(30), 4)
