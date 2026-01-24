import unittest
from mbpp_215_code import List

from 215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_single_tuple(self):
        self.assertEqual(decode_list([(1, 2)]), [(1, [0, 1])])

    def test_single_list(self):
        self.assertEqual(decode_list([[1, 2]]), [(1, range(2))])

    def test_multiple_tuples(self):
        self.assertEqual(decode_list([(1, 2), (3, 4)]), [(1, [0, 1]), (3, [2, 3])])

    def test_multiple_lists(self):
        self.assertEqual(decode_list([[1, 2], [3, 4]]), [(1, range(2)), (3, range(4, 8))])

    def test_mixed_tuples_and_lists(self):
        self.assertEqual(decode_list([(1, 2), [3, 4], (5, 6)]), [(1, [0, 1]), (3, range(4, 6)), (5, [4, 5])])
