import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_singly([]), [])

    def test_single_list(self):
        self.assertEqual(extract_singly([[1, 2, 3]]), [1, 2, 3])

    def test_multiple_lists(self):
        self.assertEqual(extract_singly([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(extract_singly([[1, 2, 2], [2, 3, 3], [3, 4, 4]]), [1, 2, 3, 4])

    def test_single_element_lists(self):
        self.assertEqual(extract_singly([[1], [2], [3]]), [1, 2, 3])

    def test_empty_sublists(self):
        self.assertEqual(extract_singly([[], [], []]), [])
