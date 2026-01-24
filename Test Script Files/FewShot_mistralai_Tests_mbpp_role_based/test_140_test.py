import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_singly([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_empty_list(self):
        self.assertEqual(extract_singly([]), [])

    def test_single_element_list(self):
        self.assertEqual(extract_singly([[1]]), [1])

    def test_single_element_list_with_duplicates(self):
        self.assertEqual(extract_singly([[1, 1]]), [1])

    def test_list_with_duplicates(self):
        self.assertEqual(extract_singly([[1, 2, 2], [3, 4, 4], [5, 6, 6]]), [1, 2, 3, 4, 5, 6])

    def test_list_with_only_duplicates(self):
        self.assertEqual(extract_singly([[2, 2], [2, 2]]), [2])

    def test_list_with_empty_inner_list(self):
        self.assertEqual(extract_singly([[], [1], [2, 3]]), [1, 2, 3])
