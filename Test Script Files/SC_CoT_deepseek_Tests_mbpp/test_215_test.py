import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(decode_list([[2, 1], [3, 2], [4, 3]]), [1, 1, 2, 2, 3, 3, 4])

    def test_single_element(self):
        self.assertEqual(decode_list([[1, 0]]), [])

    def test_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_negative_numbers(self):
        self.assertEqual(decode_list([[-2, 1], [-3, 2], [-4, 3]]), [-1, -1, -2, -2, -3, -3, -4])

    def test_zero_repeat(self):
        self.assertEqual(decode_list([[0, 0]]), [0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decode_list("invalid input")
