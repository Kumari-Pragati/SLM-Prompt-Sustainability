import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(decode_list([(1, 2), (3, 4), (5, 6)]), [(1, 0), (1, 1), (3, 2), (3, 3), (5, 4), (5, 5)])

    def test_empty_list(self):
        self.assertListEqual(decode_list([]), [])

    def test_single_tuple(self):
        self.assertListEqual(decode_list([(1, 2)]), [(1, 0), (1, 1)])

    def test_single_list(self):
        self.assertListEqual(decode_list([[1, 2]]), [(1, range(0, 1))])

    def test_mixed_types(self):
        self.assertListEqual(decode_list([(1, 2), [3, 4]]), [(1, 0), (1, 1), (3, range(0, 4))])

    def test_negative_start(self):
        self.assertListEqual(decode_list([(-1, 2), (3, 4)]), [(3, range(0, 4))])

    def test_zero_start(self):
        self.assertListEqual(decode_list([(0, 2), (3, 4)]), [(3, range(0, 4))])

    def test_end_beyond_list(self):
        self.assertListEqual(decode_list([(1, 5), (3, 4)]), [(1, 0), (1, 1), (1, 2), (1, 3), (3, 0), (3, 1), (3, 2), (3, 3)])
