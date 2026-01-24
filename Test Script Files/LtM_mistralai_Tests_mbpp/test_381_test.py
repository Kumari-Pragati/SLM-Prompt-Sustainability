import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(index_on_inner_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0),
                         [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(index_on_inner_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1),
                         [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(index_on_inner_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2),
                         [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_edge_cases(self):
        self.assertEqual(index_on_inner_list([], 0), [])
        self.assertEqual(index_on_inner_list([[1]], 0), [[1]])
        self.assertEqual(index_on_inner_list([[1]], 1), [[1]])
        self.assertEqual(index_on_inner_list([[1]], 2), [[1]])

        self.assertEqual(index_on_inner_list([[1], [2], [3]], 0), [[1], [2], [3]])
        self.assertEqual(index_on_inner_list([[1], [2], [3]], 1), [[1], [2], [3]])
        self.assertEqual(index_on_inner_list([[1], [2], [3]], 2), [[1], [2], [3]])

    def test_complex_cases(self):
        self.assertEqual(index_on_inner_list([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 0),
                         [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        self.assertEqual(index_on_inner_list([[1, 2, 3], [1, 2, -3], [1, 2, 3]], 1),
                         [[1, 1, 1], [-2, 2, 2], [3, 3, 3]])
        self.assertEqual(index_on_inner_list([[1, 2, 3], [1, 2, -3], [1, 2, 3]], 2),
                         [[1, 1, 1], [1, 2, -2], [1, 1, 3]])
