import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(decode_list([(1, [0])]), [(1, [0])])

    def test_list_of_lists(self):
        self.assertEqual(decode_list([(1, [0]), (2, [1, 2])]), [(1, [0]), (2, [1, 2])])

    def test_list_with_mixed_types(self):
        self.assertEqual(decode_list([(1, [0]), 'hello', (3, [4])]), [(1, [0]), (3, [4])])

    def test_list_with_negative_numbers(self):
        self.assertEqual(decode_list([(-1, [0]), (2, [1, 2])]), [(-1, [0]), (2, [1, 2])])

    def test_list_with_zero(self):
        self.assertEqual(decode_list([(0, [0])]), [(0, [0])])

    def test_list_with_large_numbers(self):
        self.assertEqual(decode_list([(100, [0]), (200, [1, 2])]), [(100, [0]), (200, [1, 2])])
