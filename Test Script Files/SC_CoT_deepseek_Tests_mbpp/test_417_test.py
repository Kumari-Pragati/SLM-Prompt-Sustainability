import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_typical_case(self):
        Input = [('a', 1, 2, 3), ('b', 4, 5, 6), ('a', 7, 8, 9)]
        expected_output = [('a', 1, 2, 3, 7, 8, 9), ('b', 4, 5, 6)]
        self.assertEqual(group_tuples(Input), expected_output)

    def test_empty_input(self):
        Input = []
        expected_output = []
        self.assertEqual(group_tuples(Input), expected_output)

    def test_single_tuple(self):
        Input = [('a', 1, 2, 3)]
        expected_output = [('a', 1, 2, 3)]
        self.assertEqual(group_tuples(Input), expected_output)

    def test_duplicate_keys(self):
        Input = [('a', 1, 2, 3), ('a', 4, 5, 6)]
        expected_output = [('a', 1, 2, 3, 4, 5, 6)]
        self.assertEqual(group_tuples(Input), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            group_tuples('not a list')
