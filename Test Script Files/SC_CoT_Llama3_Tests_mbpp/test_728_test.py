import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_list([], []), [])

    def test_edge_case_single_element_lists(self):
        self.assertEqual(sum_list([1], [2]), [3])
        self.assertEqual(sum_list([1], []), [1])

    def test_edge_case_lists_of_different_lengths(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5]), [5, 7])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sum_list(123, [1, 2, 3])

    def test_invalid_input_non_list2(self):
        with self.assertRaises(TypeError):
            sum_list([1, 2, 3], 'abc')
