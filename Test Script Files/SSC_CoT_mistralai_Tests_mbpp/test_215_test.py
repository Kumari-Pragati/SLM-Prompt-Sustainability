import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(decode_list([(1, 2), (3, 4), (5, 6)]), [(1, range(2)), (3, range(4)), (5, range(6))])

    def test_empty_input(self):
        self.assertListEqual(decode_list([]), [])

    def test_single_input(self):
        self.assertListEqual(decode_list([(1, 2)]), [(1, range(2))])

    def test_negative_start(self):
        self.assertListEqual(decode_list([(-1, 2)]), [(1, range(-1, 0))])

    def test_zero_start(self):
        self.assertListEqual(decode_list([(0, 2)]), [(0, range(2))])

    def test_end_beyond_list(self):
        self.assertListEqual(decode_list([(1, 5), (3, 6)]), [(1, range(5)), (3, range(6))])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decode_list([(1, 'a'), (2, 3)])
