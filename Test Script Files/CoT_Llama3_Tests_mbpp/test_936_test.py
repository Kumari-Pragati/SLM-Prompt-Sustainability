import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):
    def test_typical_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['a', 'c', 'b']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1), ('c', 3), ('b', 2)])

    def test_empty_input(self):
        test_list = []
        ord_list = []
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [])

    def test_single_element_input(self):
        test_list = [('a', 1)]
        ord_list = ['a']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('a', 1)])

    def test_invalid_input_type(self):
        test_list = 'invalid'
        ord_list = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            re_arrange_tuples(test_list, ord_list)

    def test_invalid_input_value(self):
        test_list = [('a', 1), ('b', 2)]
        ord_list = 'invalid'
        with self.assertRaises(TypeError):
            re_arrange_tuples(test_list, ord_list)
