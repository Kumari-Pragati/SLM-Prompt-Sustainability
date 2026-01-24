import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_singly([]), [])

    def test_single_element(self):
        self.assertEqual(extract_singly([[1]]), [1])

    def test_multiple_elements(self):
        self.assertEqual(extract_singly([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(extract_singly([[1, 2, 2, 3, 3, 3], [2, 3, 4, 4, 5]]), [1, 2, 3, 4, 5])

    def test_empty_inner_list(self):
        self.assertEqual(extract_singly([[], [1, 2, 3]]), [1, 2, 3])

    def test_empty_test_list(self):
        self.assertEqual(extract_singly([]), [])
