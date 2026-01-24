import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10, 11, 12, 13, 14)]
        K = 3
        expected_output = [(1, 2, 3), (6, 7, 8, 9)]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_empty_list(self):
        test_list = []
        K = 2
        expected_output = []
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_all_tuples_of_length_K(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        K = 2
        expected_output = []
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_all_tuples_of_length_not_K(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        K = 3
        expected_output = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_mixed_lengths(self):
        test_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10, 11, 12, 13, 14)]
        K = 2
        expected_output = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10, 11, 12, 13, 14)]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10, 11, 12, 13, 14)]
        K = 'two'
        with self.assertRaises(TypeError):
            remove_tuples(test_list, K)
