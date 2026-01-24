import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_Fac(1), 1)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 1)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(6), 1)
        self.assertEqual(count_Fac(7), 2)
        self.assertEqual(count_Fac(8), 2)
        self.assertEqual(count_Fac(9), 1)
        self.assertEqual(count_Fac(10), 2)
        self.assertEqual(count_Fac(12), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(1), 1)
        self.assertEqual(count_Fac(20), 8)
        self.assertEqual(count_Fac(30), 9)
        self.assertEqual(count_Fac(40), 12)
        self.assertEqual(count_Fac(50), 16)
        self.assertEqual(count_Fac(60), 16)
        self.assertEqual(count_Fac(70), 15)
        self.assertEqual(count_Fac(80), 18)
        self.assertEqual(count_Fac(90), 20)
        self.assertEqual(count_Fac(100), 24)

    def test_special_cases(self):
        self.assertEqual(count_Fac(120), 22)
        self.assertEqual(count_Fac(240), 36)
        self.assertEqual(count_Fac(360), 48)
        self.assertEqual(count_Fac(480), 60)
        self.assertEqual(count_Fac(600), 72)
        self.assertEqual(count_Fac(720), 84)
        self.assertEqual(count_Fac(840), 96)
        self.assertEqual(count_Fac(960), 108)
        self.assertEqual(count_Fac(1080), 120)
