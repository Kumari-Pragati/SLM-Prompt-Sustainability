import unittest
from mbpp_335_code import ap_sum

class TestArithmeticProgressionSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(ap_sum(1, 5, 2), 14)

    def test_edge_condition(self):
        self.assertEqual(ap_sum(0, 1, 0), 0)

    def test_boundary_condition(self):
        self.assertEqual(ap_sum(100, 100, 1), 10000)

    def test_negative_numbers(self):
        self.assertEqual(ap_sum(-1, 5, 2), 8)

    def test_zero_difference(self):
        self.assertEqual(ap_sum(1, 5, 0), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            ap_sum("a", 5, 2)
