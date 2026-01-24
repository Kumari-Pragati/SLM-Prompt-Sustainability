import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tup_string((1, 2, 3)), '123')

    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(tup_string(('a',)), 'a')

    def test_multiple_elements_tuple(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_non_string_elements(self):
        self.assertEqual(tup_string((1, 2, 3)), '123')

    def test_mixed_type_elements(self):
        self.assertEqual(tup_string(('a', 2, 'c')), 'ac2')

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tup_string('')
