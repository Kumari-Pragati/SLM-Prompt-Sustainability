import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):
    def test_simple_gcd(self):
        self.assertEqual(recur_gcd(4, 6), 2)
        self.assertEqual(recur_gcd(8, 12), 4)
        self.assertEqual(recur_gcd(15, 25), 5)

    def test_zero_input(self):
        self.assertEqual(recur_gcd(0, 12), 12)
        self.assertEqual(recur_gcd(12, 0), 12)

    def test_one_input(self):
        self.assertEqual(recur_gcd(1, 12), 1)
        self.assertEqual(recur_gcd(12, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(recur_gcd(0, 0), 0)
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(2, 2), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            recur_gcd('a', 12)
        with self.assertRaises(TypeError):
            recur_gcd(12, 'b')
