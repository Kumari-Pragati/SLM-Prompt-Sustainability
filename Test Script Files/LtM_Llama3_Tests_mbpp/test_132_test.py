import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(tup_string(('a',)), 'a')

    def test_multiple_elements_tuple(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_tuple_with_spaces(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_tuple_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            tup_string((1, 2, 3))

    def test_tuple_with_mixed_types(self):
        with self.assertRaises(TypeError):
            tup_string(('a', 1, 'b'))

    def test_tuple_with_empty_string(self):
        self.assertEqual(tup_string(('', 'b')), 'b')

    def test_tuple_with_empty_string_at_end(self):
        self.assertEqual(tup_string(('a', '', 'c')), 'ac')
