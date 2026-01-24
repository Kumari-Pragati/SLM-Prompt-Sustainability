import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(remove_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1),
                              [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertListEqual(remove_column([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], 2),
                              [['a', None, 'c'], ['d', None, 'f'], ['g', None, 'i']])

    def test_edge_cases(self):
        self.assertListEqual(remove_column([[1, 2, 3]], 0), [[1, 2, 3]])
        self.assertListEqual(remove_column([], 0), [])
        self.assertListEqual(remove_column([[1], [2]], 1), [[1], [2]])
        self.assertListEqual(remove_column([[1], [2]], 2), [[1], []])
        self.assertListEqual(remove_column([[1], [2]], -1), [[1], [2]])

    def test_complex_cases(self):
        self.assertListEqual(remove_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2),
                              [[1, 2, 3], [4, 5, 6], [7, None, 9]])
        self.assertListEqual(remove_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3),
                              [[1, 2, None], [4, 5, 6], [7, 8, 9]])
