import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_singly([]), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_singly([[1]]), [1])

    def test_multiple_elements_list(self):
        self.assertListEqual(extract_singly([[1, 2], [2, 3], [3, 1]]), [1, 2, 3])

    def test_duplicate_elements_list(self):
        self.assertListEqual(extract_singly([[1, 2], [2, 1], [2, 3]]), [1, 2, 3])

    def test_nested_lists(self):
        self.assertListEqual(extract_singly([[1, [2, 3]], [4, [2, 5]], [6, [2, 3]]]), [1, 2, 3, 4, 5, 6])
