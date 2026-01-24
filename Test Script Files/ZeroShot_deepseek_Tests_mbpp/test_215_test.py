import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_single_element(self):
        self.assertEqual(decode_list([1]), [(1, [0])])

    def test_multiple_elements(self):
        self.assertEqual(decode_list([1, 2]), [(1, [0]), (2, [0])])

    def test_nested_list(self):
        self.assertEqual(decode_list([[1, 2], 3]), [(1, [0]), (1, [1]), (3, [0])])

    def test_mixed_elements(self):
        self.assertEqual(decode_list([1, [2, 3], 4]), [(1, [0]), (2, [0]), (2, [1]), (4, [0])])
