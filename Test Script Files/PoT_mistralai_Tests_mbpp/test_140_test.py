import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(extract_singly([[1, 2, 3], [4, 5, 1], [2, 3, 4]]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertListEqual(extract_singly([]), [])

    def test_single_inner_list(self):
        self.assertListEqual(extract_singly([[1]]), [1])

    def test_single_element_inner_list(self):
        self.assertListEqual(extract_singly([[1]]), [1])

    def test_duplicate_elements(self):
        self.assertListEqual(extract_singly([[1, 1], [2, 2], [3, 3]]), [1, 2, 3])

    def test_empty_inner_list(self):
        self.assertListEqual(extract_singly([[], [1], [2, 3]]), [1, 2, 3])
