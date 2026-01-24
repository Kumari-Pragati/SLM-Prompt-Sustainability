import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(extract_singly([]), [])

    def test_single_element_list(self):
        self.assertEqual(extract_singly([[1]]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(extract_singly([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_duplicates(self):
        self.assertEqual(extract_singly([[1, 2, 2, 3], [4, 5, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_empty_inner_list(self):
        self.assertEqual(extract_singly([[], [1, 2, 3]]), [1, 2, 3])

    def test_nested_lists(self):
        self.assertEqual(extract_singly([[1, 2, 3], [4, [5, 6], 7]]), [1, 2, 3, 4, 5, 6, 7])

    def test_empty_inner_list_with_duplicates(self):
        self.assertEqual(extract_singly([[], [1, 2, 2, 3], [4, 5, 5, 6]]), [1, 2, 3, 4, 5, 6])
