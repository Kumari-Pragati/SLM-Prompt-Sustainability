import unittest
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):

    def test_encode_list_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_encode_list_single_element(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_encode_list_multiple_elements(self):
        self.assertEqual(encode_list([1, 1, 2, 3, 1, 2, 2, 3, 3, 3]), 
                         [[2, 1], [1, 2], [2, 3]])

    def test_encode_list_duplicates(self):
        self.assertEqual(encode_list([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]), 
                         [[3, 1], [3, 2], [4, 3]])

    def test_encode_list_empty_group(self):
        self.assertEqual(encode_list([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 
                         [[1, 1], [2, 2], [3, 3], [4, 4]])
