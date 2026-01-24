import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Ops([10, 20, 30], 3, 10), 3)

    def test_max_value_not_divisible_by_k(self):
        self.assertEqual(min_Ops([10, 25, 30], 3, 10), -1)

    def test_single_element_array(self):
        self.assertEqual(min_Ops([10], 1, 10), 0)

    def test_empty_array(self):
        self.assertEqual(min_Ops([], 0, 10), 0)

    def test_negative_values(self):
        self.assertEqual(min_Ops([-10, -20, -30], 3, 10), 3)

    def test_k_equals_zero(self):
        self.assertEqual(min_Ops([10, 20, 30], 3, 0), -1)

    def test_k_less_than_min_array_value(self):
        self.assertEqual(min_Ops([10, 20, 30], 3, 5), -1)
