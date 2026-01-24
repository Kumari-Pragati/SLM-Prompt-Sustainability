import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case_n_is_1(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case_n_is_last_element(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case_n_is_zero(self):
        with self.assertRaises(IndexError):
            pair_OR_Sum([], 0)

    def test_edge_case_n_is_negative(self):
        with self.assertRaises(IndexError):
            pair_OR_Sum([1, 2, 3, 4, 5], -1)

    def test_edge_case_n_is_greater_than_array_length(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 10), 0)

    def test_special_case_all_elements_are_same(self):
        self.assertEqual(pair_OR_Sum([1, 1, 1, 1, 1], 5), 0)

    def test_special_case_all_elements_are_zero(self):
        self.assertEqual(pair_OR_Sum([0, 0, 0, 0, 0], 5), 0)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            pair_OR_Sum([1, 2, 3, 4, 5], 'a')

    def test_invalid_input_non_list_array(self):
        with self.assertRaises(TypeError):
            pair_OR_Sum('abc', 5)
