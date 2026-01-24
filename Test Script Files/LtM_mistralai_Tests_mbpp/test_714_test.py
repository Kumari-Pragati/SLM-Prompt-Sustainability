import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(count_Fac(1), 1)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 1)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(6), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(10), 4)
        self.assertEqual(count_Fac(12), 6)
        self.assertEqual(count_Fac(20), 9)
        self.assertEqual(count_Fac(25), 6)
        self.assertEqual(count_Fac(100), 24)

    def test_complex_scenarios(self):
        self.assertEqual(count_Fac(120), 12)
        self.assertEqual(count_Fac(220), 11)
        self.assertEqual(count_Fac(360), 15)
        self.assertEqual(count_Fac(441344), 364)
