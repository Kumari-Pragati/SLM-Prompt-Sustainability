import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edge_case_empty_list(self):
        self.assertEqual(add_list([1, 2, 3], []), [1, 2, 3])

    def test_edge_case_single_element(self):
        self.assertEqual(add_list([1], [2]), [3])

    def test_edge_case_single_element_empty_list(self):
        self.assertEqual(add_list([1], []), [1])

    def test_edge_case_empty_list_empty_list(self):
        self.assertEqual(add_list([], []), [])

    def test_edge_case_single_element_single_element(self):
        self.assertEqual(add_list([1], [1]), [2])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            add_list('a', [1, 2, 3])

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            add_list([1, 2, 3], 'a')

    def test_invalid_input_type_list_list(self):
        with self.assertRaises(TypeError):
            add_list('a', 'b')
