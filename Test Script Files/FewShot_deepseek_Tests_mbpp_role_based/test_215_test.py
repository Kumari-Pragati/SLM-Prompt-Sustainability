import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(decode_list([[1, 2], 3]), [2, 0, 0, 0])

    def test_edge_condition(self):
        self.assertEqual(decode_list([]), [])

    def test_boundary_condition(self):
        self.assertEqual(decode_list([[0, 1], 0]), [0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decode_list('invalid_input')
