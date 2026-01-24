import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_edge_case_empty_list(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))

    def test_edge_case_single_element(self):
        self.assertEqual(add_lists([1], (2,)), (2, 1))

    def test_edge_case_single_element_list(self):
        self.assertEqual(add_lists([1], ()), (1,))

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(add_lists([], (1,)), (1,))

    def test_error_case_non_list_input(self):
        with self.assertRaises(TypeError):
            add_lists('abc', (1, 2, 3))

    def test_error_case_non_tuple_input(self):
        with self.assertRaises(TypeError):
            add_lists([1, 2, 3], 'abc')
