import unittest
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_multiple_elements_list(self):
        self.assertEqual(encode_list([1, 1, 2, 3, 1, 2, 3, 4]), [[1, 1], [1, 2], [1, 3], [1, 4]])

    def test_empty_group(self):
        self.assertEqual(encode_list([1, 2, 2, 3, 3, 3]), [[1, 1], [1, 2], [2, 1], [2, 1], [3, 1], [3, 2]])

    def test_group_with_single_element(self):
        self.assertEqual(encode_list([1, 1, 1, 2, 2, 3, 3, 3]), [[1, 1], [2, 1], [3, 1]])

    def test_group_with_multiple_elements(self):
        self.assertEqual(encode_list([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]])
