import unittest
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(encode_list([1, 1, 1, 2, 2, 3]), [[3, 1], [2, 2], [1, 3]])

    def test_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_single_element(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_repeated_elements(self):
        self.assertEqual(encode_list([1, 1, 1, 1]), [[4, 1]])

    def test_mixed_elements(self):
        self.assertEqual(encode_list([1, 2, 2, 1, 1]), [[1, 1], [2, 2], [2, 1]])

    def test_large_repeated_elements(self):
        self.assertEqual(encode_list([1]*1000), [[1000, 1]])
