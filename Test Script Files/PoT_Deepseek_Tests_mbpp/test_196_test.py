import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
        K = 2
        expected_output = [(1, 2), (6,)]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_edge_case_K_zero(self):
        test_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
        K = 0
        expected_output = test_list
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_boundary_case_K_one(self):
        test_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
        K = 1
        expected_output = [(1, 2), (3, 4, 5), (7, 8, 9, 10)]
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_corner_case_empty_list(self):
        test_list = []
        K = 2
        expected_output = []
        self.assertEqual(remove_tuples(test_list, K), expected_output)

    def test_corner_case_single_tuple(self):
        test_list = [(1, 2)]
        K = 2
        expected_output = []
        self.assertEqual(remove_tuples(test_list, K), expected_output)
