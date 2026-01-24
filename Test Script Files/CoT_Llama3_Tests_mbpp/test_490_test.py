import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_symmetric([]), [])

    def test_single_element_list(self):
        self.assertEqual(extract_symmetric([(1, 1)]), [])

    def test_no_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (3, 4)]), [])

    def test_single_symmetric_pair(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1)]), [(1, 2)])

    def test_multiple_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (3, 4), (4, 3)]), [(1, 2), (2, 1), (3, 4), (4, 3)])

    def test_non_symmetric_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (3, 4), (5, 6)]), [])

    def test_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (1, 2)]), [(1, 2)])
