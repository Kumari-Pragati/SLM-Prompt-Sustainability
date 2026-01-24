import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Ops([10, 20, 30], 3, 10), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(min_Ops([10], 1, 10), 0)

    def test_edge_case_max_element_divisible_by_k(self):
        self.assertEqual(min_Ops([10, 20, 30], 3, 10), 3)

    def test_edge_case_max_element_not_divisible_by_k(self):
        self.assertEqual(min_Ops([10, 25, 30], 3, 10), -1)

    def test_invalid_input_negative_elements(self):
        with self.assertRaises(Exception):
            min_Ops([-10, 20, 30], 3, 10)

    def test_invalid_input_zero_elements(self):
        with self.assertRaises(Exception):
            min_Ops([], 0, 10)

    def test_invalid_input_negative_k(self):
        with self.assertRaises(Exception):
            min_Ops([10, 20, 30], 3, -10)
