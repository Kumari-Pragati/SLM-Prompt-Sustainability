import unittest
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(encode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_multiple_elements_list(self):
        self.assertEqual(encode_list([1, 1, 2, 2, 3, 3, 3]), [[1, 1], [2, 2], [3, 3]])

    def test_list_with_duplicates(self):
        self.assertEqual(encode_list([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]), [[1, 1], [2, 2], [3, 3]])

    def test_list_with_negative_numbers(self):
        self.assertEqual(encode_list([-1, -1, -2, -2, -3, -3, -3]), [[-1, -1], [-2, -2], [-3, -3]])

    def test_list_with_zero(self):
        self.assertEqual(encode_list([0, 0, 0]), [[0, 0]])
