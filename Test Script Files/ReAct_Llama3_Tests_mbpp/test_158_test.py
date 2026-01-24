import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)

    def test_edge_case_max(self):
        self.assertEqual(min_Ops([10, 10, 10, 10, 10], 5, 2), 2)

    def test_edge_case_min(self):
        self.assertEqual(min_Ops([1, 1, 1, 1, 1], 5, 2), 2)

    def test_edge_case_k_zero(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 0), -1)

    def test_edge_case_k_one(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 1), 2)

    def test_error_case_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], 'a', 2)

    def test_error_case_invalid_input2(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], 5, 'a')
