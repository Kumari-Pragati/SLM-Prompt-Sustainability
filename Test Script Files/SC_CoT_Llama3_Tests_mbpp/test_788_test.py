import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_typical_inputs(self):
        test_list = [1, 2, 3]
        test_str = 'hello'
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, (1, 2, 3, 'hello'))

    def test_edge_case_empty_list(self):
        test_list = []
        test_str = 'hello'
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, ('hello',))

    def test_edge_case_single_element_list(self):
        test_list = [1]
        test_str = 'hello'
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, (1, 'hello'))

    def test_edge_case_empty_string(self):
        test_list = [1, 2, 3]
        test_str = ''
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, (1, 2, 3,))

    def test_edge_case_single_element_string(self):
        test_list = [1]
        test_str = 'hello'
        result = new_tuple(test_list, test_str)
        self.assertEqual(result, (1, 'hello'))

    def test_invalid_input_non_list(self):
        test_list = 'hello'
        test_str = 'world'
        with self.assertRaises(TypeError):
            new_tuple(test_list, test_str)

    def test_invalid_input_non_string(self):
        test_list = [1, 2, 3]
        test_str = 123
        with self.assertRaises(TypeError):
            new_tuple(test_list, test_str)
