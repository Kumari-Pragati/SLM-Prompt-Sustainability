import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_single_group(self):
        numbers = [1, 1, 1, 1, 1]
        n = 1
        expected = [1]
        self.assertEqual(extract_elements(numbers, n), expected)

    def test_multiple_groups(self):
        numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        n = 2
        expected = [1, 2, 3]
        self.assertEqual(extract_elements(numbers, n), expected)

    def test_empty_list(self):
        numbers = []
        n = 1
        expected = []
        self.assertEqual(extract_elements(numbers, n), expected)

    def test_single_element_group(self):
        numbers = [1, 2, 3, 4, 5]
        n = 5
        expected = [5]
        self.assertEqual(extract_elements(numbers, n), expected)

    def test_no_groups(self):
        numbers = [1, 2, 3, 4, 5, 6]
        n = 10
        expected = []
        self.assertEqual(extract_elements(numbers, n), expected)
