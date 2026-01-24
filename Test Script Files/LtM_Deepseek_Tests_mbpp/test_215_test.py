import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(decode_list([1, 2, 3]), [0, 1, 2])

    def test_empty_input(self):
        self.assertEqual(decode_list([]), [])

    def test_single_element_input(self):
        self.assertEqual(decode_list([4]), [4, 0])

    def test_negative_numbers(self):
        self.assertEqual(decode_list([-1, -2]), [-1, -2, 0])

    def test_large_numbers(self):
        self.assertEqual(decode_list([100, 200]), list(range(100)) + list(range(200)))

    def test_mixed_input(self):
        self.assertEqual(decode_list([1, 'two', 3]), [0, 'two', 0])

    def test_list_with_list(self):
        self.assertEqual(decode_list([[2, 3], 4]), [(3, range(2)), 4, 0])

    def test_nested_list(self):
        self.assertEqual(decode_list([[1, 2], [3, 4]]), [0, 1, 0, 2, 0, 3, 0, 4])
