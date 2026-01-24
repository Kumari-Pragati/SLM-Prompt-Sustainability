import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):
    def test_typical_use_case(self):
        Input = [('a', 1, 2, 3), ('b', 4, 5), ('a', 6)]
        expected_output = [('a', 1, 2, 3, 6), ('b', 4, 5)]
        self.assertEqual(group_tuples(Input), expected_output)

    def test_edge_condition(self):
        Input = [('a', 1), ('b', 2), ('c', 3)]
        expected_output = [('a', 1), ('b', 2), ('c', 3)]
        self.assertEqual(group_tuples(Input), expected_output)

    def test_boundary_condition(self):
        Input = [()]
        expected_output = [()]
        self.assertEqual(group_tuples(Input), expected_output)

    def test_invalid_input(self):
        Input = [('a', 1, 2, 'b'), ('c', 3)]
        with self.assertRaises(TypeError):
            group_tuples(Input)
