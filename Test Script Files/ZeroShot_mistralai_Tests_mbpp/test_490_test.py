import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):

    def test_empty_list(self):
        self.assertSetEqual(set(), extract_symmetric([]))

    def test_single_element(self):
        self.assertSetEqual(set(), extract_symmetric([(1, 1)]))

    def test_symmetric_pair(self):
        self.assertSetEqual({((1, 2), (2, 1))}, extract_symmetric([(1, 2), (2, 1)]))

    def test_multiple_symmetric_pairs(self):
        self.assertSetEqual({((1, 2), (2, 1)), ((3, 4), (4, 3)), ((5, 6), (6, 5))},
                             extract_symmetric([(1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5)]))

    def test_non_symmetric_pairs(self):
        self.assertSetEqual(set(), extract_symmetric([(1, 2), (2, 3), (3, 4)]))

    def test_duplicate_pairs(self):
        self.assertSetEqual({((1, 2), (2, 1)), ((1, 2), (2, 1))}, extract_symmetric([(1, 2), (2, 1), (1, 2)]))
