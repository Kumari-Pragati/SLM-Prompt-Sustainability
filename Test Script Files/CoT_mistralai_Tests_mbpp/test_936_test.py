import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(re_arrange_tuples([], []), [])
        self.assertEqual(re_arrange_tuples([], [1]), [(1, None)])
        self.assertEqual(re_arrange_tuples([], [1, 2]), [(1, None), (2, None)])

    def test_single_tuple(self):
        self.assertEqual(re_arrange_tuples([(1, 2)], [1]), [(1, 2)])
        self.assertEqual(re_arrange_tuples([(1, 2)], [2]), [(2, 1)])

    def test_multiple_tuples(self):
        self.assertEqual(re_arrange_tuples([(1, 2), (3, 4)], [1, 2, 3]), [(1, 2), (3, 4)])
        self.assertEqual(re_arrange_tuples([(1, 2), (3, 4)], [2, 1, 3]), [(2, 1), (3, 4)])
        self.assertEqual(re_arrange_tuples([(1, 2), (3, 4)], [3, 1, 2]), [(3, 4), (1, 2)])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, re_arrange_tuples, [1, 2], 1)
        self.assertRaises(TypeError, re_arrange_tuples, [(1, 2)], "string")
        self.assertRaises(ValueError, re_arrange_tuples, [(1, 2), (3, 4)], [5])
