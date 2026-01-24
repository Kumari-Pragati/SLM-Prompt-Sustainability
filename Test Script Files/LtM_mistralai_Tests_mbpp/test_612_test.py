import unittest
from mbpp_612_code import merge

class TestMerge(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(merge([[1, 2], [3, 4]]), [[[1, 3]], [[2, 4]]])
        self.assertEqual(merge([['a', 'b'], ['c', 'd']]), [[['a', 'c']], [['b', 'd']]])
        self.assertEqual(merge([[1, 2, 3], [4, 5, 6]]), [[[1, 4]], [[2, 5]], [[3, 6]]])

    def test_edge_cases(self):
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([[]]), [[[]]])
        self.assertEqual(merge([[1]]), [[[1]]])
        self.assertEqual(merge([[1, 2], [3]]), [[[1], [3]]])
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6]]), [[[1, 3], [2, 4]], [ [5, 6] ]])

    def test_complex_cases(self):
        self.assertEqual(merge([[1, 2], [3], [4, 5]]), [[[1], [3]], [[2], []], [[4, 5]]])
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6, 7]]), [[[1, 3], [2, 4]], [[5], [6]], [ [7] ]])
        self.assertEqual(merge([[1, 2, 3], [4, 5], [6, 7, 8]]), [[[1, 4, 6]], [[2, 5, 7]], [[3, 8]]])
