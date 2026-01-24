import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):

    def test_typical_input(self):
        lst = [['a', 'b'], ['c', 'd']]
        self.assertEqual(Extract(lst), ['a', 'c'])

    def test_edge_case_empty_list(self):
        lst = []
        self.assertEqual(Extract(lst), [])

    def test_edge_case_single_element_list(self):
        lst = [['a', 'b']]
        self.assertEqual(Extract(lst), ['a'])

    def test_edge_case_single_element_list_with_empty_element(self):
        lst = [['a', ''], ['c', 'd']]
        self.assertEqual(Extract(lst), ['a', 'c'])

    def test_edge_case_list_with_empty_elements(self):
        lst = [['a', ''], ['', 'd']]
        self.assertEqual(Extract(lst), ['a', 'd'])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            Extract('not a list')

    def test_invalid_input_non_list_with_nested_list(self):
        with self.assertRaises(TypeError):
            Extract([['a', 'b'], 'not a list'])

    def test_invalid_input_list_with_non_string_elements(self):
        lst = [[1, 2], [3, 4]]
        with self.assertRaises(TypeError):
            Extract(lst)

    def test_invalid_input_list_with_non_string_elements_and_empty_elements(self):
        lst = [[1, 2], ['', 4]]
        with self.assertRaises(TypeError):
            Extract(lst)
