import unittest
from mbpp_687_code import recur_gcd

class TestRecurGCD(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(recur_gcd(36, 24), 12)
        self.assertEqual(recur_gcd(25, 10), 5)
        self.assertEqual(recur_gcd(49, 121), 1)

    def test_edge_cases(self):
        self.assertEqual(recur_gCD(0, 10), 10)
        self.assertEqual(recur_gCD(1, 0), 1)
        self.assertEqual(recur_gCD(1, 1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(recur_gCD(-10, 10), 10)
        self.assertEqual(recur_gCD(10, -10), 10)
        self.assertEqual(recur_gCD(0, 0), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, recur_gCD, "a", 10)
        self.assertRaises(TypeError, recur_gCD, 10, "b")
