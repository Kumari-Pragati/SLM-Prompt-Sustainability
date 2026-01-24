import unittest
from mbpp_157_code import encode_list

class TestEncodeList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(encode_list([1, 1, 1, 2, 2, 3, 3, 3, 3]), [[3, 1], [2, 2], [2, 3], [4, 3]])

    def test_edge_condition(self):
        self.assertEqual(encode_list([]), [])

    def test_boundary_condition(self):
        self.assertEqual(encode_list([1]), [[1, 1]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            encode_list(123)
