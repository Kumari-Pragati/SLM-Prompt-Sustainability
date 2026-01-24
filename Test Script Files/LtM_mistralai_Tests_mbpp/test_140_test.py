import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):

    def test_simple_list(self):
        self.assertListEqual(extract_singly([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_empty_list(self):
        self.assertListEqual(extract_singly([]), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_singly([[1]]), [1])

    def test_duplicate_elements(self):
        self.assertListEqual(extract_singly([[1, 1], [2, 2], [3, 3]]), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertListEqual(extract_singly([[-1, -2, -3], [4, 5, 6], [-7, -8, -9]]), [-1, -2, -3, 4, 5, 6, -7, -8, -9])

    def test_floats(self):
        self.assertListEqual(extract_singly([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]), [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])

    def test_strings(self):
        self.assertListEqual(extract_singly([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

    def test_mixed_types(self):
        self.assertListEqual(extract_singly([[1, 'a', 3.14], [2, 'b', 2.718], [4, 'c', 0]]), [1, 'a', 3.14, 2, 'b', 2.718, 4, 'c', 0])
