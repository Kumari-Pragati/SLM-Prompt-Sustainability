import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_typical_input(self):
        test_list = [1, 2, 3]
        test_str = 'a'
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, (1, 2, 3, 'a'))

    def test_empty_list(self):
        test_list = []
        test_str = 'a'
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, ('a',))

    def test_single_element_list(self):
        test_list = [1]
        test_str = 'a'
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, (1, 'a'))

    def test_multiple_element_list(self):
        test_list = [1, 2, 3, 4]
        test_str = 'a'
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, (1, 2, 3, 4, 'a'))

    def test_non_string_input(self):
        test_list = [1, 2, 3]
        test_str = 123
        with self.assertRaises(TypeError):
            new_tuple(test_list, test_str)

    def test_non_list_input(self):
        test_list = 'abc'
        test_str = 'a'
        with self.assertRaises(TypeError):
            new_tuple(test_list, test_str)
