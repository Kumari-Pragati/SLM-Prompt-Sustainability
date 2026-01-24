import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_decode_list(self):
        self.assertEqual(decode_list([[3, 1], [2, 0]]), [(1, [0, 1, 2]), (0, [0, 1, 2])])
        self.assertEqual(decode_list([[3, 1], [2, 0], [1, 0]]), [(1, [0, 1, 2]), (0, [0, 1, 2]), (0, [0, 1])])
        self.assertEqual(decode_list([[3, 1], [2, 0], [1, 0], [1, 1]]), [(1, [0, 1, 2]), (0, [0, 1, 2]), (0, [0, 1]), (1, [0, 1])])
        self.assertEqual(decode_list([[3, 1]]), [(1, [0, 1, 2])])
        self.assertEqual(decode_list([[3, 1], [2, 0], [1, 0], [1, 1], [2, 1]]), [(1, [0, 1, 2]), (0, [0, 1, 2]), (0, [0, 1]), (1, [0, 1]), (1, [0, 1])])
