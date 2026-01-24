import unittest
from mbpp_491_code import sum_gp

class TestSumGP(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_gp(10, 5, 2), 34.375)

    def test_edge_cases(self):
        self.assertEqual(sum_gp(0, 0, 0), 0)
        self.assertEqual(sum_gp(0, 1, 0), 1)
        self.assertEqual(sum_gp(1, 0, 0), 1)
        self.assertEqual(sum_gp(1, 1, 1), 1)

    def test_negative_inputs(self):
        with self.assertRaises(ValueError):
            sum_gp(-10, 5, 2)
        with self.assertRaises(ValueError):
            sum_gp(10, -5, 2)
        with self.assertRaises(ValueError):
            sum_gp(10, 5, -2)

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            sum_gp(1, 0, 1)
