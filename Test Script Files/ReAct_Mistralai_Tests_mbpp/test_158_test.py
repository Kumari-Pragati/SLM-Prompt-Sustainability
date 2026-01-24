import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_empty_array(self):
        self.assertRaises(ValueError, min_Ops, [], 1, 2)

    def test_single_element_array(self):
        self.assertEqual(min_Ops([1], 1, 1), 0)
        self.assertRaises(ValueError, min_Ops, [1], 1, 0)

    def test_normal_case(self):
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 1), 3)
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 2), 1.5)
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 3), 1)

    def test_k_greater_than_n(self):
        self.assertRaises(ValueError, min_Ops, [1, 2, 3], 2, 4)

    def test_k_less_than_1(self):
        self.assertRaises(ValueError, min_Ops, [1, 2, 3], 4, 0)

    def test_arr_greater_than_k(self):
        self.assertRaises(ValueError, min_Ops, [10, 20, 30], 1, 1)

    def test_arr_less_than_k(self):
        self.assertRaises(ValueError, min_Ops, [1, 2], 3, 1)

    def test_non_integer_k(self):
        self.assertRaises(TypeError, min_Ops, [1, 2, 3], 4, 3.5)

    def test_negative_arr(self):
        self.assertRaises(TypeError, min_Ops, [-1, -2, -3], 1, 1)
