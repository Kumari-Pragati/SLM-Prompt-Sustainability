import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(extract_singly([]), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_singly([[1]]), [1])

    def test_multiple_elements_list(self):
        self.assertListEqual(extract_singly([[1, 2], [2, 3], [3, 1]]), [1, 2, 3])

    def test_duplicate_elements_in_list(self):
        self.assertListEqual(extract_singly([[1, 2, 2], [2, 3], [3, 1]]), [1, 2, 3])

    def test_empty_inner_list(self):
        self.assertListEqual(extract_singly([[]]), [])

    def test_mixed_types_list(self):
        self.assertRaises(TypeError, extract_singly, [[1, 'a'], [2, 3], [3, 'b']])

    def test_non_iterable_input(self):
        self.assertRaises(TypeError, extract_singly, 123)
