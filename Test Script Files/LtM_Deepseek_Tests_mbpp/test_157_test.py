import unittest
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(encode_list([1, 1, 1, 2, 2, 3]), [[3, 1], [2, 2], [1, 3]])

    def test_empty_input(self):
        self.assertEqual(encode_list([]), [])

    def test_single_element_input(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_repeated_elements_input(self):
        self.assertEqual(encode_list([1, 1, 1, 1]), [[4, 1]])

    def test_mixed_elements_input(self):
        self.assertEqual(encode_list([1, 2, 2, 3, 3, 3]), [[1, 1], [2, 2], [3, 3]])
