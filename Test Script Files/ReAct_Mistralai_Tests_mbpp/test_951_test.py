import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(max_similar_indices([(1, 2)], [(3, 4)]), [(1, 4)])
        self.assertEqual(max_similar_indices([(3, 4)], [(1, 2)]), [(3, 2)])

    def test_identical_lists(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(1, 2), (3, 4)]), [(1, 2), (3, 4)])

    def test_different_lengths(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(1, 2)]), [(1, 2)])
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4)])

    def test_negative_values(self):
        self.assertEqual(max_similar_indices([(-1, 2), (3, 4)], [(1, 2), (-3, 4)]), [(-1, 2), (3, 4)])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_similar_indices([(1, 2), (3, 4)], [(1, 2), "string"])
