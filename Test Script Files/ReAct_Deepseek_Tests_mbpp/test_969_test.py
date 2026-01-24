import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
        expected_output = [('a', 1, 3), ('b', 2), ('c', 4)]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_single_tuple(self):
        test_list = [('a', 1)]
        expected_output = [('a', 1)]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_no_matching_first_element(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        expected_output = [('a', 1), ('b', 2), ('c', 3)]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_all_matching_first_element(self):
        test_list = [('a', 1), ('a', 2), ('a', 3)]
        expected_output = [('a', 1, 2, 3)]
        self.assertEqual(join_tuples(test_list), expected_output)

    def test_error_case(self):
        test_list = [('a', 1, 2), ('b', 2)]
        with self.assertRaises(TypeError):
            join_tuples(test_list)
