import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(max_similar_indices([[1, 2]], [[3, 4]]), [(3, 4)])

    def test_equal_lists(self):
        self.assertEqual(max_similar_indices([[1, 2], [3, 4]], [[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_lists_with_max_values(self):
        self.assertEqual(max_similar_indices([[10, 20], [30, 40]], [[5, 15], [25, 35]]), [(30, 40)])

    def test_lists_with_min_values(self):
        self.assertEqual(max_similar_indices([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [(7, 8)])

    def test_lists_with_max_and_min_values(self):
        self.assertEqual(max_similar_indices([[10, 20], [30, 40]], [[5, 15], [25, 35]]), [(30, 40)])

    def test_lists_with_negative_values(self):
        self.assertEqual(max_similar_indices([[-10, -20], [-30, -40]], [[-5, -15], [-25, -35]]), [(-5, -15)])

    def test_lists_with_zero_values(self):
        self.assertEqual(max_similar_indices([[0, 0], [0, 0]], [[0, 0], [0, 0]]), [[0, 0]])
