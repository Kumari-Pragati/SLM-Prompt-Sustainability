import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):
    def test_typical_input(self):
        test_list = [[1, 2, 3], 4, 5, 6]
        K = 3
        result = remove_tuples(test_list, K)
        self.assertEqual(result, [4, 5, 6])

    def test_edge_case1(self):
        test_list = [[1, 2, 3], 4, 5, 6]
        K = 0
        result = remove_tuples(test_list, K)
        self.assertEqual(result, test_list)

    def test_edge_case2(self):
        test_list = [[1, 2, 3], 4, 5, 6]
        K = 7
        result = remove_tuples(test_list, K)
        self.assertEqual(result, [])

    def test_edge_case3(self):
        test_list = [[1, 2, 3], 4, 5, 6]
        K = 6
        result = remove_tuples(test_list, K)
        self.assertEqual(result, [4, 5])

    def test_special_case(self):
        test_list = [[1, 2, 3], 4, 5, 6]
        K = 2
        result = remove_tuples(test_list, K)
        self.assertEqual(result, [4, 5, 6])

    def test_invalid_input1(self):
        test_list = [[1, 2, 3], 4, 5, 6]
        K = 'a'
        with self.assertRaises(TypeError):
            remove_tuples(test_list, K)

    def test_invalid_input2(self):
        test_list = [[1, 2, 3], 4, 5, 6]
        K = None
        with self.assertRaises(TypeError):
            remove_tuples(test_list, K)
