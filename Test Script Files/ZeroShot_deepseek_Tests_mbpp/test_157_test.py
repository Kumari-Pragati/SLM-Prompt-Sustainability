import unittest
from mbpp_157_code import groupby
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(encode_list(['a']), [[1, 'a']])

    def test_repeated_elements(self):
        self.assertEqual(encode_list(['a', 'a', 'b', 'b', 'b', 'c']), [[2, 'a'], [3, 'b'], [1, 'c']])

    def test_unique_elements(self):
        self.assertEqual(encode_list(['a', 'b', 'c']), [[1, 'a'], [1, 'b'], [1, 'c']])

    def test_large_list(self):
        self.assertEqual(encode_list(['a'] * 10000 + ['b'] * 20000 + ['c'] * 30000), 
                         [[10000, 'a'], [20000, 'b'], [30000, 'c']])
