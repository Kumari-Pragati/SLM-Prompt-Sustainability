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
        self.assertEqual(extract_singly([[1, 1, 2, 2, 3, 3]]), [1, 2, 3])

    def test_empty_inner_list(self):
        self.assertEqual(extract_singly([[], [1, 2, 3]]), [1, 2, 3])

    def test_edge_case(self):
        self.assertEqual(extract_singly([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_singly("invalid_input")
