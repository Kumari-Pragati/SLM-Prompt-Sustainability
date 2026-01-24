import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(extract_symmetric([]), [])

    def test_single_pair(self):
        self.assertEqual(extract_symmetric([(1, 2)]), [(1, 2)])

    def test_multiple_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 3), (3, 4)]), [(1, 2), (2, 3)])

    def test_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (3, 4)]), [(1, 2)])

    def test_empty_set(self):
        self.assertEqual(extract_symmetric([]), [])

    def test_set_with_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (3, 4)]), [(1, 2)])

    def test_set_with_no_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 2), (3, 4)]), [(1, 2)])

    def test_set_with_no_duplicates_and_empty_list(self):
        self.assertEqual(extract_symmetric([]), [])

    def test_set_with_duplicates_and_empty_list(self):
        self.assertEqual(extract_symmetric([]), [])
