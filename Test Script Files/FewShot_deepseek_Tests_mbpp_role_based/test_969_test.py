import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', 1, 'b'), ('b', 2, 'c'), ('a', 3, 'd')]
        expected_output = [('a', 1, 'b', 3, 'd'), ('b', 2, 'c')]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_edge_condition(self):
        test_list = [()]
        expected_output = [()]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_boundary_condition(self):
        test_list = [('a',), ('a',)]
        expected_output = [('a',)]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_different_start_values(self):
        test_list = [('a', 1, 'b'), ('c', 2, 'd')]
        expected_output = [('a', 1, 'b'), ('c', 2, 'd')]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(join_tuples(test_list), expected_output)
