import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [1, 2, 3]
        test_str = 'a'
        result = new_tuple(test_list, test_str)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (1, 2, 3, 'a'))

    def test_empty_list(self):
        test_list = []
        test_str = 'b'
        result = new_tuple(test_list, test_str)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, ('b',))

    def test_single_element_list(self):
        test_list = [4]
        test_str = 'c'
        result = new_tuple(test_list, test_str)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (4, 'c'))

    def test_multiple_elements_list(self):
        test_list = [5, 6, 7]
        test_str = 'd'
        result = new_tuple(test_list, test_str)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (5, 6, 7, 'd'))

    def test_non_string_input(self):
        test_list = [8, 9, 10]
        test_str = 11
        with self.assertRaises(TypeError):
            new_tuple(test_list, test_str)
