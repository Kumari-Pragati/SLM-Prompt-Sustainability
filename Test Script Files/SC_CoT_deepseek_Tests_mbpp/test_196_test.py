import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (3, 4, 5), (6,), ()]
        K = 2
        expected_output = [(1, 2), (3, 4, 5), (6,)]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_edge_case_empty_list(self):
        test_list = []
        K = 2
        expected_output = []
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_edge_case_all_tuples_of_length_K(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        K = 2
        expected_output = []
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_edge_case_single_tuple(self):
        test_list = [(1, 2)]
        K = 2
        expected_output = []
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_corner_case_tuple_with_length_greater_than_K(self):
        test_list = [(1, 2, 3), (4, 5, 6, 7)]
        K = 2
        expected_output = [(1, 2, 3), (4, 5, 6, 7)]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_invalid_input_negative_K(self):
        test_list = [(1, 2), (3, 4, 5), (6,)]
        K = -1
        with self.assertRaises(ValueError):
            remove_tuples(test_list, K)

    def test_invalid_input_non_integer_K(self):
        test_list = [(1, 2), (3, 4, 5), (6,)]
        K = 'two'
        with self.assertRaises(TypeError):
            remove_tuples(test_list, K)
