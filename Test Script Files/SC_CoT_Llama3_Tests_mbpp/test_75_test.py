import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_typical_input(self):
        test_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        K = 10
        self.assertEqual(find_tuples(test_list, K), '[[10, 20, 30], [40, 50, 60], [70, 80, 90]]')

    def test_edge_case(self):
        test_list = [[10, 20, 30], [40, 50, 60]]
        K = 20
        self.assertEqual(find_tuples(test_list, K), '[[10, 20, 30]]')

    def test_edge_case2(self):
        test_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        K = 100
        self.assertEqual(find_tuples(test_list, K), '[[10, 20, 30], [40, 50, 60], [70, 80, 90]]')

    def test_empty_list(self):
        test_list = []
        K = 10
        self.assertEqual(find_tuples(test_list, K), '[]')

    def test_single_tuple(self):
        test_list = [[10, 20, 30]]
        K = 10
        self.assertEqual(find_tuples(test_list, K), '[[10, 20, 30]]')

    def test_invalid_input_type(self):
        test_list = [[10, 20, 30]]
        K = 'invalid'
        with self.assertRaises(TypeError):
            find_tuples(test_list, K)

    def test_invalid_input_value(self):
        test_list = [[10, 20, 30]]
        K = -5
        with self.assertRaises(TypeError):
            find_tuples(test_list, K)
