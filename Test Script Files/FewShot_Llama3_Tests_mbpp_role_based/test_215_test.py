import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(decode_list([[3, 1], [2, 0]]), [(1, range(3)), (0, range(2))])

    def test_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(decode_list([[5, 0]]), [(0, [0, 1, 2, 3, 4]))

    def test_nested_list(self):
        self.assertEqual(decode_list([[3, 1], [2, 0], [1, 0]]), [(1, range(3)), (0, range(2)), (0, range(1))])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decode_list("not a list")
