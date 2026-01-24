import unittest
from mbpp_157_code import (chain, islice, repeat)
from 157_code import encode_list

class TestEncodeList(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(encode_list([1, 1, 2, 3, 3, 4, 4, 4, 5]),
                         [[1, 1], [2, 2], [1, 3], [1, 4], [1, 5]])

    def test_edge_cases(self):
        self.assertEqual(encode_list([]), [])
        self.assertEqual(encode_list([1]), [[1, 1]])
        self.assertEqual(encode_list([1, 1]), [[1, 1], [1, 1]])
        self.assertEqual(encode_list([1, 1, 1]), [[1, 1], [1, 1], [1, 1]])

    def test_boundary_cases(self):
        self.assertEqual(encode_list(list(chain(*[repeat(i, i) for i in range(1, 6)]))),
                         [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
        self.assertEqual(encode_list(list(chain(*[repeat(i, i) for i in range(1, 6)]) + [6])),
                         [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 6]])
        self.assertEqual(encode_list(list(chain(*[repeat(i, i) for i in range(1, 6)])) + [6] * 5),
                         [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 6], [1, 6], [1, 6], [1, 6], [1, 6]])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, encode_list, 123)
        self.assertRaises(TypeError, encode_list, (1, 2, 3))
