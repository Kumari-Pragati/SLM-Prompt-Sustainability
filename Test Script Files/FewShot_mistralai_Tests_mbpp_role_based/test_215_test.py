import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_single_tuple(self):
        self.assertEqual(decode_list([(1, 2)]), [(1, range(2))])

    def test_single_list(self):
        self.assertEqual(decode_list([[1, 2]]), [(1, range(2))])

    def test_multiple_tuples(self):
        self.assertEqual(decode_list([(1, 2), (3, 4)]), [(1, range(2)), (3, range(4))])

    def test_multiple_lists(self):
        self.assertEqual(decode_list([[1, 2], [3, 4]]), [(1, range(2)), (3, range(4))])

    def test_mixed_tuples_and_lists(self):
        self.assertEqual(decode_list([(1, 2), [3, 4], (5, 6)]), [(1, range(2)), (3, range(4)), (5, range(6))])

    def test_negative_start_index(self):
        with self.assertRaises(ValueError):
            decode_list([[(0, -1)]])

    def test_negative_end_index(self):
        with self.assertRaises(ValueError):
            decode_list([[(1, -1)]])
