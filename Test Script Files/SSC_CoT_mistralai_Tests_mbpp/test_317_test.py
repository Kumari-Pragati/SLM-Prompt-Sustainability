import unittest
from mbpp_317_code import chain, islice, repeat
from functools import reduce

from 317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(modified_encode([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]),
                         [1, [2], [3, 3, 3], [4, 4, 4, 4]])
        self.assertEqual(modified_encode([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]),
                         [1, [2], [3, 3, 3], [4, 4, 4, 4], [5]])

    def test_edge_cases(self):
        self.assertEqual(modified_encode([]), [])
        self.assertEqual(modified_encode([1]), [1])
        self.assertEqual(modified_encode([1, 1]), [1, [1]])
        self.assertEqual(modified_encode([1, 1, 1]), [1, 1, [1]])
        self.assertEqual(modified_encode([1, 1, 1, 1]), [1, 1, 1, [1]])
        self.assertEqual(modified_encode([1, 1, 1, 1, 1]), [1, 1, 1, 1, [1]])

    def test_boundary_cases(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, [1]])
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1, [1]])
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1, 1, [1]])
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1, 1, 1, [1]])
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1, 1, 1, 1, [1]])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, modified_encode, 123)
        self.assertRaises(TypeError, modified_encode, (1, 2, 3))
        self.assertRaises(TypeError, modified_encode, {'a': 1, 'b': 2})
        self.assertRaises(TypeError, modified_encode, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
