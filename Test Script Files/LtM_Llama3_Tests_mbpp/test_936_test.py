import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('b', 2)], ['a', 'b']), [('a', 1), ('b', 2)])

    def test_empty_input(self):
        self.assertEqual(re_arrange_tuples([], ['a', 'b']), [])

    def test_empty_order_list(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('b', 2)], []), [])

    def test_empty_test_list(self):
        self.assertEqual(re_arrange_tuples([], []), [])

    def test_repeated_keys(self):
        self.assertEqual(re_arrange_tuples([('a', 1), ('a', 2), ('b', 3)], ['a', 'b']), [('a', 1), ('a', 2), ('b', 3)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            re_arrange_tuples('test', ['a', 'b'])

    def test_invalid_order_type(self):
        with self.assertRaises(TypeError):
            re_arrange_tuples([('a', 1), ('b', 2)], 'order')
