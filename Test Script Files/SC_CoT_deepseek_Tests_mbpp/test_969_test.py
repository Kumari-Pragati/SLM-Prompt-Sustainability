import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 1, 'b'), ('a', 2, 'c'), ('b', 3, 'd')]
        expected_output = [('a', 1, 'b', 2, 'c'), ('b', 3, 'd')]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_single_tuple(self):
        test_list = [('a', 1, 'b')]
        expected_output = [('a', 1, 'b')]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_no_matching_first_element(self):
        test_list = [('a', 1, 'b'), ('c', 2, 'd')]
        expected_output = [('a', 1, 'b'), ('c', 2, 'd')]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [('a', 1, 'b'), 'c', ('a', 2, 'd')]
        with self.assertRaises(TypeError):
            join_tuples(test_list)
