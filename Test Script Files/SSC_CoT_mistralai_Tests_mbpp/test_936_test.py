import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('b', 2), ('c', 3)], ['c', 'a', 'b']), [('c', 3), ('a', 1), ('b', 2)])

    def test_edge_case_empty_lists(self):
        self.assertEqual(re_arrange_tuples([], []), [])
        self.assertEqual(re_arrange_tuples([('a', 1)], []), [])
        self.assertEqual(re_arrange_tuples([], ['a']), [])

    def test_edge_case_single_element(self):
        self.assertEqual(re_arrange_tuples([('a', 1)], ['a']), [('a', 1)])

    def test_edge_case_duplicate_keys(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('a', 2)], ['a']), [('a', 1), ('a', 2)])

    def test_edge_case_invalid_ordering(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('b', 2), ('c', 3)], ['b', 'c', 'a']), [('b', 2), ('c', 3), ('a', 1)])

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, re_arrange_tuples, [1, 2], [3])
        self.assertRaises(TypeError, re_arrange_tuples, [('a', 1), 2], [3])
        self.assertRaises(TypeError, re_arrange_tuples, [('a', 1)], [3, 2])
