import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_typical_case(self):
        input_data = [('a', 1, 2, 3), ('b', 4, 5), ('a', 6, 7)]
        expected_output = [('a', 1, 2, 3, 6, 7), ('b', 4, 5)]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_single_tuple(self):
        input_data = [('a', 1, 2, 3)]
        expected_output = [('a', 1, 2, 3)]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_empty_input(self):
        input_data = []
        expected_output = []
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_duplicate_keys(self):
        input_data = [('a', 1, 2, 3), ('a', 4, 5)]
        expected_output = [('a', 1, 2, 3, 4, 5)]
        self.assertEqual(group_tuples(input_data), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            group_tuples('invalid input')
