import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_symmetric([]), set())

    def test_single_element_list(self):
        self.assertEqual(extract_symmetric([(1, 1)]), set())

    def test_no_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 3), (3, 4)]), set())

    def test_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1)]), {(1, 2)})

    def test_multiple_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (3, 4), (4, 3)]), {(1, 2), (3, 4)})

    def test_no_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 1), (2, 2), (3, 3)]), set())

    def test_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 1), (1, 1), (2, 2), (2, 2)]), set())
