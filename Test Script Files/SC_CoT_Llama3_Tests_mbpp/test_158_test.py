import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)

    def test_edge_case_max_value(self):
        self.assertEqual(min_Ops([10, 20, 30, 40, 50], 5, 2), 2)

    def test_edge_case_min_value(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(min_Ops([10], 1, 2), -1)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(min_Ops([0], 1, 2), 0)

    def test_edge_case_k_zero(self):
        self.assertEqual(min_Ops([10, 20, 30, 40, 50], 5, 0), -1)

    def test_edge_case_k_negative(self):
        self.assertEqual(min_Ops([10, 20, 30, 40, 50], 5, -2), -1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            min_Ops("hello", 5, 2)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3], "hello", 2)

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3], 5, "hello")
