import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(Extract([[1], [2, 3], [4, 5, 6]]), [1, 3, 6])
        self.assertEqual(Extract([['a'], ['b', 'c'], ['d', 'e', 'f']]), ['a', 'c', 'f'])

    def test_edge_cases(self):
        self.assertEqual(Extract([]), [])
        self.assertEqual(Extract([[1]]), [1])
        self.assertEqual(Extract([[1, 2]]), [2])

    def test_complex(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])
        self.assertEqual(Extract([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), ['c', 'f', 'i'])
