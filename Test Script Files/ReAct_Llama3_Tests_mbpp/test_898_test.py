import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_single_group(self):
        self.assertEqual(extract_elements([1, 1, 1, 2, 2, 3, 3, 3], 3), [3])

    def test_multiple_groups(self):
        self.assertEqual(extract_elements([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5], 3), [3, 5])

    def test_no_groups(self):
        self.assertEqual(extract_elements([1, 2, 3, 4, 5], 3), [])

    def test_single_group_length_one(self):
        self.assertEqual(extract_elements([1, 1, 1, 2, 2, 3, 3, 3], 1), [1, 2, 3])

    def test_group_length_zero(self):
        with self.assertRaises(IndexError):
            extract_elements([1, 1, 1, 2, 2, 3, 3, 3], 0)

    def test_empty_input(self):
        self.assertEqual(extract_elements([], 3), [])

    def test_single_element(self):
        self.assertEqual(extract_elements([1], 1), [1])
