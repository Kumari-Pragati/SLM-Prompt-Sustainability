import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 60)

    def test_edge_case_max_three(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6]), 60)

    def test_edge_case_min_two(self):
        self.assertEqual(maximum_product([-1, -2, 3, 4, 5, 6]), 60)

    def test_edge_case_max_three_min_two(self):
        self.assertEqual(maximum_product([-1, -2, 3, 4, 5, 6, 7]), 60)

    def test_edge_case_max_three_min_two_negative(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6, -7]), -30)

    def test_edge_case_max_three_min_two_zero(self):
        self.assertEqual(maximum_product([0, 0, 1, 2, 3, 4, 5]), 0)

    def test_edge_case_max_three_min_two_zero_negative(self):
        self.assertEqual(maximum_product([-1, -2, 0, 0, 1, 2, 3]), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            maximum_product("abc")

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            maximum_product([])
