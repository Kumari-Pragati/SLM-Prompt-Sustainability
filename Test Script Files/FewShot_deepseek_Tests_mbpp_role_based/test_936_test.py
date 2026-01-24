import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['b', 'a', 'c']
        expected_output = [('b', 2), ('a', 1), ('c', 3)]
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_output)

    def test_edge_condition(self):
        test_list = []
        ord_list = []
        expected_output = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_output)

    def test_boundary_condition(self):
        test_list = [('a', 1)]
        ord_list = ['a']
        expected_output = [('a', 1)]
        self.assertEqual(re_arrange_tuples(test_list, ord_list), expected_output)

    def test_invalid_input(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['b', 'a', 1]  # Invalid input, 1 is not a string
        with self.assertRaises(TypeError):
            re_arrange_tuples(test_list, ord_list)
