import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(decode_list([]), [])

    def test_single_tuple(self):
        self.assertListEqual(decode_list([(1, 2)]), [(1, range(2))])

    def test_single_list(self):
        self.assertListEqual(decode_list([[1, 2]]), [(1, range(2))])

    def test_multiple_tuples(self):
        self.assertListEqual(decode_list([(1, 2), (3, 4)]), [(1, range(2)), (3, range(4))])

    def test_multiple_lists(self):
        self.assertListEqual(decode_list([[1, 2], [3, 4]]), [(1, range(2)), (3, range(4))])

    def test_mixed_types(self):
        self.assertRaises(TypeError, decode_list, [1, (2, 3)])

    def test_negative_start(self):
        self.assertRaises(ValueError, decode_list, [([0, -1],)])

    def test_negative_end(self):
        self.assertRaises(ValueError, decode_list, [([0, 1], [0, -1])])

    def test_invalid_list_element(self):
        self.assertRaises(TypeError, decode_list, [([0, 1], 'invalid')])
