import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(new_tuple([1, 2, 3], 'a'), (1, 2, 3, 'a'))

    def test_empty_list(self):
        self.assertEqual(new_tuple([], 'a'), ('a',))

    def test_empty_str(self):
        self.assertEqual(new_tuple([1, 2, 3], ''), (1, 2, 3, ''))

    def test_single_element_list(self):
        self.assertEqual(new_tuple([1], 'a'), (1, 'a'))

    def test_multiple_element_list(self):
        self.assertEqual(new_tuple([1, 2, 3, 4], 'a'), (1, 2, 3, 4, 'a'))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            new_tuple([1, 2, 3], 123)
