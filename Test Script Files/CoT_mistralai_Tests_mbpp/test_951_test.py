import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_same_lists(self):
        self.assertEqual(max_similar_indices([(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)]), [(2, 2)])

    def test_different_lengths(self):
        self.assertEqual(max_similar_indices([(0, 0), (1, 1), (2, 2)], [(0, 0), (1, 1)]), [(1, 1)])

    def test_empty_lists(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(max_similar_indices([(0, 0)], [(1, 1)]), [(0, 0)])

    def test_opposites(self):
        self.assertEqual(max_similar_indices([(0, 0), (1, 1)], [(1, 1), (0, 0)]), [(1, 1)])

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            max_similar_indices([1, 2, 3], [4, 5, 6])

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            max_similar_indices([(0, 'a'), (1, 'b')], [(0, 0), (1, 1)])
