import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_max_similar_indices(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 6), (7, 8)]),
                         [((1, 2), (5, 6)), ((3, 4), (7, 8))])
        self.assertEqual(max_similar_indices([(10, 20), (30, 40)], [(50, 60), (70, 80)]),
                         [((10, 20), (50, 60)), ((30, 40), (70, 80))])
        self.assertEqual(max_similar_indices([(100, 200), (300, 400)], [(500, 600), (700, 800)]),
                         [((100, 200), (500, 600)), ((300, 400), (700, 800))])
