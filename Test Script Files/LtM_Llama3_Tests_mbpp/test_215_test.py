import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(decode_list([[1, 2]]), [(2, [0, 1])))

    def test_empty(self):
        self.assertEqual(decode_list([]), [])

    def test_single_element(self):
        self.assertEqual(decode_list([1]), [(1, [0])))

    def test_nested_lists(self):
        self.assertEqual(decode_list([[1, 2], [3, 4]]), [(2, [0, 1]), (4, [0, 1])))

    def test_edge_cases(self):
        self.assertEqual(decode_list([[0, 0]]), [(0, [0])))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decode_list('invalid')
