import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(extract_singly([[1, 2, 3], [2, 3, 4]]), [1, 2, 3, 4])

    def test_empty_input(self):
        self.assertEqual(extract_singly([]), [])

    def test_single_element_input(self):
        self.assertEqual(extract_singly([[1]]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(extract_singly([[1, 1, 1], [2, 2, 2]]), [1, 2])

    def test_large_input(self):
        self.assertEqual(extract_singly([list(range(1, 1001)), list(range(1, 1001))]), list(range(1, 1001)))

    def test_negative_numbers(self):
        self.assertEqual(extract_singly([[-1, -2, -3], [-2, -3, -4]]), [-1, -2, -3, -4])

    def test_mixed_numbers(self):
        self.assertEqual(extract_singly([[1, -1, 2], [-1, 2, 3]]), [1, -1, 2, 3])
