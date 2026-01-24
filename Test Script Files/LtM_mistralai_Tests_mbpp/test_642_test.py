import unittest
from mbpp_642_code import range
from six.moves.collections import OrderedDict

from six42_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1]]), [[1, 2]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2]]), [[1, 2]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [1, 3]]), [[1, 2], [1, 3]])

    def test_edge_and_boundary(self):
        self.assertListEqual(remove_similar_row([[]]), [[]])
        self.assertListEqual(remove_similar_row([[1]]), [[1]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [2, 1]]), [[1, 2]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [1, 2], [1, 2]]), [[1, 2]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [1, 2], [1, 3]]), [[1, 2], [1, 3]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [1, 2], [1, 3], [1, 3]]), [[1, 2], [1, 3]])

    def test_complex(self):
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [1, 3], [3, 1]]), [[1, 2], [1, 3]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [1, 3], [3, 1], [1, 2, 3]]), [[1, 2], [1, 3]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [1, 3], [3, 1], [1, 2, 3], [1, 2, 3]]), [[1, 2], [1, 3]])
        self.assertListEqual(remove_similar_row([[1, 2], [2, 1], [1, 2], [1, 3], [3, 1], [1, 2, 3], [1, 2, 3], [1, 2, 4]]), [[1, 2], [1, 3], [1, 2, 4]])
