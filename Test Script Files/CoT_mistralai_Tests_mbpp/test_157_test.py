import unittest
from mbpp_157_code import islice, chain, repeat
from functools import reduce

from 157_code import encode_list

class TestEncodeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_list_with_duplicates(self):
        self.assertEqual(encode_list([1, 1, 2, 2, 3, 3, 3]), [[2, 1], [2, 2], [1, 3], [3, 3], [3, 3]])

    def test_list_with_no_duplicates(self):
        self.assertEqual(encode_list([1, 2, 3]), [[1, 1], [1, 2], [1, 3]])

    def test_list_with_long_sequences(self):
        self.assertEqual(encode_list(list(repeat(1, 10))), [[10, 1]])

    def test_list_with_short_sequences(self):
        self.assertEqual(encode_list(list(islice(repeat(1, 5), 3))), [[3, 1], [1, 1], [1, 1]])

    def test_list_with_mixed_sequences(self):
        self.assertEqual(encode_list(list(chain([1, 1, 2], repeat(2, 3), [3]))), [[2, 1], [3, 2], [3, 2], [3, 2], [3, 3]])

    def test_list_with_invalid_input(self):
        self.assertRaises(TypeError, encode_list, [1.0, 2])
