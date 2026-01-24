import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_remove_tuples_typical(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 3
        expected_output = [[1, 2], [4, 5], [7, 8]]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_remove_tuples_edge_case1(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        K = 3
        expected_output = [[1, 2], [4, 5], [7, 8], [10, 11, 12]]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_remove_tuples_edge_case2(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 0
        expected_output = []
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_remove_tuples_edge_case3(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 10
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_remove_tuples_invalid_input1(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 'a'
        with self.assertRaises(TypeError):
            remove_tuples(test_list, K)

    def test_remove_tuples_invalid_input2(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = -1
        with self.assertRaises(TypeError):
            remove_tuples(test_list, K)
