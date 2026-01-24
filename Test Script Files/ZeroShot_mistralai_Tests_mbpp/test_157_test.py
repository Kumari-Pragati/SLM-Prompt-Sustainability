import unittest
from mbpp_157_code import groupby

def encode_list(list1):
    return [[len(list(group)), key] for key, group in groupby(list1)]

class TestEncodeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_duplicate_elements_list(self):
        self.assertEqual(encode_list([1, 1, 2, 1, 2, 3]), [[2, 1], [1, 1], [2, 2], [1, 3]])

    def test_unique_elements_list(self):
        self.assertEqual(encode_list([1, 2, 3, 4]), [[1, 1], [1, 2], [1, 3], [1, 4]])
