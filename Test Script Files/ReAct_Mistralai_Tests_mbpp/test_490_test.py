import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):

    def test_empty_list(self):
        self.assertSetEqual(set(), extract_symmetric([]))

    def test_single_element(self):
        self.assertSetEqual({(1, 1)}, extract_symmetric([(1, 1)]))

    def test_symmetric_pair(self):
        self.assertSetEqual({((1, 2), (2, 1)), ((3, 4), (4, 3))},
                             extract_symmetric([(1, 2), (2, 1), (3, 4), (4, 3)]))

    def test_multiple_symmetric_pairs(self):
        self.assertSetEqual({((1, 2), (2, 1)), ((3, 4), (4, 3)), ((5, 6), (6, 5))},
                             extract_symmetric([(1, 2), (2, 1), (3, 4), (4, 3), (5, 6), (6, 5)]))

    def test_reverse_order(self):
        self.assertSetEqual({((1, 2), (2, 1)), ((3, 4), (4, 3))},
                             extract_symmetric([(2, 1), (1, 2), (3, 4), (4, 3)]))

    def test_duplicate_elements(self):
        self.assertSetEqual({((1, 2), (2, 1)), ((1, 2), (2, 1))},
                             extract_symmetric([(1, 2), (1, 2)]))

    def test_duplicate_symmetric_pairs(self):
        self.assertSetEqual({((1, 2), (2, 1)), ((1, 2), (2, 1)), ((3, 4), (4, 3))},
                             extract_symmetric([(1, 2), (1, 2), (2, 1), (3, 4), (4, 3)]))

    def test_non_symmetric_pair(self):
        self.assertSetEqual(set(), extract_symmetric([(1, 2), (2, 3)]))

    def test_non_numeric_elements(self):
        self.assertSetEqual(set(), extract_symmetric([('a', 'b'), (1, 2)]))

    def test_negative_numbers(self):
        self.assertSetEqual({((-1, -2), (-2, -1))}, extract_symmetric([(-1, -2), (-2, -1)]))
