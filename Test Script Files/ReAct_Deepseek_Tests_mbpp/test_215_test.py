import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(decode_list([[1, 2], 3]), [(2, [0]), (3, [0])])

    def test_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(decode_list([4]), [(4, [0])])

    def test_list_with_single_element(self):
        self.assertEqual(decode_list([[5, 1], 6]), [(1, [0]), (6, [0])])

    def test_list_with_zero_range(self):
        self.assertEqual(decode_list([[0, 0], 7]), [])

    def test_list_with_negative_range(self):
        self.assertEqual(decode_list([[1, -1], 8]), [(1, [])])

    def test_list_with_large_range(self):
        self.assertEqual(decode_list([[10, 10], 9]), [(10, list(range(10)))])

    def test_mixed_types_in_list(self):
        with self.assertRaises(TypeError):
            decode_list([[1, 2], 'string'])
