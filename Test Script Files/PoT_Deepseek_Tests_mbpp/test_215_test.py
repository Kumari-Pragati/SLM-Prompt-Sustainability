import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(decode_list([[1, 2], [3, 4]]), [('2', range(1)), ('4', range(3))])

    def test_edge_case_empty_list(self):
        self.assertEqual(decode_list([]), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(decode_list([[5, 1]]), [('1', range(5))])

    def test_corner_case_single_number(self):
        self.assertEqual(decode_list([7]), [('0', [0])])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decode_list('invalid_input')
