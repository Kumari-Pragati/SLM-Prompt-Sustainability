import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_simple_list_of_tuples(self):
        self.assertListEqual(decode_list([(1, 2), (3, 4)]), [(1, range(2)), (3, range(4))])

    def test_empty_list(self):
        self.assertListEqual(decode_list([]), [])

    def test_single_tuple(self):
        self.assertListEqual(decode_list([(1, 2)]), [(1, range(2))])

    def test_single_number(self):
        self.assertListEqual(decode_list([1]), [(1, [0])])

    def test_list_of_numbers(self):
        self.assertListEqual(decode_list([1, 2, 3]), [(1, [0]), (2, [1]), (3, [2])])

    def test_list_of_tuples_with_negative_start(self):
        self.assertListEqual(decode_list([(-1, 2), (3, 4)]), [(3, range(4, 0, -1)), (1, range(2))])

    def test_list_of_tuples_with_negative_end(self):
        self.assertListEqual(decode_list([(1, -1)]), [(1, range(0, -1, -1))])
