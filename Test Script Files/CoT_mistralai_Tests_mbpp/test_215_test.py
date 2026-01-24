import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_single_tuple(self):
        self.assertEqual(decode_list([(1, 2)]), [(1, [0, 1])])

    def test_multiple_tuples(self):
        self.assertEqual(decode_list([(1, 2), (3, 4)]), [(1, [0, 1]), (3, [2, 3])])

    def test_list_of_lists(self):
        self.assertEqual(decode_list([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]),
                         [(1, [0, 0]), (2, [0, 1]), (3, [1, 0]), (4, [1, 1]),
                          (5, [2, 0]), (6, [2, 1]), (7, [3, 0]), (8, [3, 1])])

    def test_list_of_tuples_and_lists(self):
        self.assertEqual(decode_list([(1, 2), [(3, 4), (5, 6)], (7, 8)]),
                         [(1, [0, 0]), (2, [0, 1]), (3, [1, 0]), (4, [1, 1]),
                          (5, [1, 2]), (6, [1, 3]), (7, [2, 0]), (8, [2, 1])])

    def test_invalid_input(self):
        self.assertRaises(TypeError, decode_list, [1, 2])
