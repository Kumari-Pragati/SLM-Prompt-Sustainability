import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_symmetric([]), set())

    def test_single_element(self):
        self.assertEqual(extract_symmetric([(1, 2)]), set())

    def test_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1)]), {(1, 2)})

    def test_non_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 3)]), set())

    def test_multiple_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (3, 4), (4, 3)]), {(1, 2), (3, 4)})

    def test_duplicate_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (1, 2)]), {(1, 2)})

    def test_unsorted_pairs(self):
        self.assertEqual(extract_symmetric([(2, 1), (1, 2)]), {(1, 2)})
