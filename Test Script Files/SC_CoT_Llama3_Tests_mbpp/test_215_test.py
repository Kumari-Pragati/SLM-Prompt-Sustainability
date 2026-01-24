import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(decode_list([[1, 2], [3, 4]]), [(2, range(1)), (4, range(1))])

    def test_edge_case_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(decode_list([[1, 2]]), [(2, range(1))])

    def test_edge_case_single_element_non_list(self):
        self.assertEqual(decode_list([1]), [(1, [0])])

    def test_edge_case_single_element_non_list_with_non_integer(self):
        with self.assertRaises(TypeError):
            decode_list(['a'])

    def test_edge_case_single_element_non_list_with_non_integer_list(self):
        with self.assertRaises(TypeError):
            decode_list([['a', 'b']])

    def test_edge_case_single_element_non_list_with_non_integer_list_nested(self):
        with self.assertRaises(TypeError):
            decode_list([['a', ['b', 'c']]])

    def test_edge_case_single_element_non_list_with_non_integer_list_nested_depth2(self):
        with self.assertRaises(TypeError):
            decode_list([['a', ['b', ['c', 'd']]]])

    def test_edge_case_single_element_non_list_with_non_integer_list_nested_depth3(self):
        with self.assertRaises(TypeError):
            decode_list([['a', ['b', ['c', ['d', 'e']]]])

    def test_edge_case_single_element_non_list_with_non_integer_list_nested_depth4(self):
        with self.assertRaises(TypeError):
            decode_list([['a', ['b', ['c', ['d', ['e', 'f']]]])
